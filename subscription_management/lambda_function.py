import ast
import logging
import os
import sys
import codecs
import hashlib
import hmac
import base64
import boto3
import requests

import simplejson as json
from datetime import datetime
from requests_oauthlib import OAuth1Session
from sendgrid import SendGridAPIClient
from boto3.dynamodb.conditions import Key, Attr
from email_validator import validate_email, EmailNotValidError

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

dynamo = boto3.resource('dynamodb', region_name="us-east-1")
table = dynamo.Table('bugalert-subscriptions-prod')

sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))

ses = boto3.client('ses', region_name="us-east-1")
hmacsecret = os.getenv('HMACSECRET')
hmacsecret = codecs.encode(hmacsecret)

TEXTEMALL_BASE_DOMAIN = "rest.text-em-all.com"
sess = OAuth1Session(os.getenv('TEXT_EM_ALL_ID'),
                     client_secret=os.getenv('TEXT_EM_ALL_SECRET'),
                     resource_owner_key=os.getenv('TEXT_EM_ALL_TOKEN'))


def respond_error(err, origin, status=400):
    response = {
        'statusCode': status,
        'body': f"{{\"error\": \"{err}\"}}",
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': origin,
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Expose-Headers': 'Content-Type',
            'Access-Control-Allow-Methods': 'GET, POST, OPTIONS, HEAD'
        },
    }
    print(response)
    return response

def respond_success(msg, origin):
    response = {
        'statusCode': '200',
        'body': msg,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': origin,
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Expose-Headers': 'Content-Type',
            'Access-Control-Allow-Methods': 'GET, POST, OPTIONS, HEAD'
        },
    }
    print(response)
    return response

def lambda_handler(event, context):
    headers = event.get('headers')
    headers = {k.lower():v for k,v in headers.items()}
    logger.info(
        f"{headers.get('x-forwarded-for', 'no-ip')} "
        f"{event.get('httpMethod', 'no-method')} "
        f"{event.get('path', 'no-path')} "
        f"{headers.get('user-agent', 'no-ua')} "
        f"{headers.get('referer', 'no-referer')} "
        f"{headers.get('origin', 'no-origin')}"
    )
    method = event.get('httpMethod')
    origin = headers.get('origin')

    path = event.get('path')[1:]
    if not path or len(path) != 6 or not path.isalpha():
        return respond_error("Unsupported path '{}'".format(path), origin)

    allowed_origins = ['https://bugalert.org', 'http://localhost:8000']
    if not headers.get('origin') or headers.get('origin') not in allowed_origins:
         return respond_error("Unsupported origin '{}'".format(headers.get('origin', '')), origin)
    elif method == 'OPTIONS':
        return respond_success("", origin)
    elif method == 'GET' and path == 'health':
        return respond_success("OK", origin)

    body = event.get('body')
    if not body:
        return respond_error("No request body", origin)
    body = json.loads(body)
    email = body.get('email')

    if not email:
        return respond_error("No email field value", origin)

    try:
      # Validate email
      valid = validate_email(email)
      # Update with the normalized form.
      email = valid.email
    except EmailNotValidError as e:
      # email is not valid, exception message is human-readable
      return respond_error("Email field is not valid: '{}'".format(str(e)), origin)

    if method == 'POST' and path == 'listup':
        # RPC to dump the contact list from dynamo into telephony provider.
        # A future improvement could be made to authenticate this, but for the moment,
        # I don't forsee anyone DoS-ing this endpoint causing any harm.
        if not os.getenv('API_KEY') or not body.get('api_key'):
            return respond_error("API key not set or sent.", origin)

        if not hmac.compare_digest(os.getenv('API_KEY'), body.get('api_key')):
            return respond_error("API key invalid.", origin)

        email_file_id, sms_file_id, phone_file_id = upload_contact_list(body.get('category'))
        json_content = f"{{\"status\": \"success\", \"email_file_id\": \"{email_file_id}\", \"sms_file_id\": \"{sms_file_id}\", \"phone_file_id\": \"{phone_file_id}\"}}"
        return respond_success(json_content, origin)
    elif method == 'POST' and path == 'verify':
        # Fire off email to confirm the user is allowed to make subscription changes.
        locally_computed_hmac = hmac.new(hmacsecret, codecs.encode(email), hashlib.sha256).digest()
        signature = base64.urlsafe_b64encode(locally_computed_hmac).decode('utf8').rstrip("=")
        msg_body = f"Please visit the following URL to verify your email address: " \
                   f"https://bugalert.org/content/pages/my-subscriptions.html" \
                   f"?signature={signature}&email={email}"
        ses.send_email(
            Destination={
                'ToAddresses': [
                    email,
                ],
            },
            Message={
                'Body': {
                    #'Html': {
                    #    'Charset': 'UTF-8',
                    #    'Data': BODY_HTML,
                    #},
                    'Text': {
                        'Charset': 'UTF-8',
                        'Data': msg_body,
                    },
                },
                'Subject': {
                    'Charset': 'UTF-8',
                    'Data': 'Bug Alert Email Verification',
                },
            },
            Source="Bug Alert <no-reply@bugalert.org>",
        )

        return respond_success("{\"status\": \"success\"}", origin)

    # Get the signature bytes
    signature = body.get('signature')
    if not signature:
        return respond_error("No signature", origin)
    padding = 4 - (len(signature) % 4)
    signature = signature + ("=" * padding)
    signature = base64.urlsafe_b64decode(signature)

    # Compare the signature
    locally_computed_hmac = hmac.new(hmacsecret, codecs.encode(email), hashlib.sha256).digest()
    if not hmac.compare_digest(signature, locally_computed_hmac):
        return respond_error("Signature failed validation", origin, status=401)

    # At this point, this is authenticated traffic
    if method == 'POST' and path == 'return':
        response = table.get_item(
            Key={
                'email': email
            }
        )
        item = response.get('Item')

        if item:
            item = json.dumps(item)
            return respond_success(item, origin)
        else:
            return respond_error("Record not found", origin, status=404)

    elif method == 'POST' and path == 'update':
        categories = ["frameworks_libs_components", "operating_systems", "services_system_applications", "end_user_applications", "test"]

        phone_number = body.get('phone_number')
        phone_country_code = body.get('phone_country_code')
        if not phone_number or not phone_country_code:
            phone_number = None
            phone_country_code = None
        elif not phone_number.isnumeric() or not phone_country_code.isnumeric():
            phone_number = None
            phone_country_code = None
        else:
            phone_number = int(phone_number)
            phone_country_code = int(phone_country_code)

        table.update_item(
            Key={
                'email': email
            },
            UpdateExpression = 'SET phone_number = :phone_number, phone_country_code = :phone_country_code, frameworks_libs_components = :frameworks_libs_components, ' \
                               'operating_systems = :operating_systems, services_system_applications = :services_system_applications, ' \
                               'end_user_applications = :end_user_applications, test = :test',
            ExpressionAttributeValues = {
                ':phone_number': phone_number,
                ':phone_country_code': phone_country_code,
                ':frameworks_libs_components': body.get('frameworks_libs_components'),
                ':operating_systems': body.get('operating_systems'),
                ':services_system_applications': body.get('services_system_applications'),
                ':end_user_applications': body.get('end_user_applications'),
                ':test': body.get('test')
            },
            ReturnValues="UPDATED_NEW"
        )

        # Send a "you are opted in" message.
        sms_opted_in = False
        phone_opted_in = False
        for category in categories:
            if body.get(category) and 's' in body.get(category):
                sms_opted_in = True
            if body.get(category) and 'p' in body.get(category):
                phone_opted_in = True

        if sms_opted_in and phone_country_code == 1 and phone_number:
            send_sms_confirmation(phone_number)

        if phone_opted_in and phone_country_code == 1 and phone_number:
            send_phone_confirmation(phone_number)

        return respond_success("{\"status\": \"success\"}", origin)

    return respond_error(f"Unsupported method {method}", origin, status=405)

def send_sms_confirmation(phone_number):
    conversation_id = make_conversation(phone_number)
    send_message(conversation_id, "Bug Alert: you are opted in to SMS-based notices. Visit https://bugalert.org/content/pages/my-subscriptions.html to manage notice subscriptions.")

def send_phone_confirmation(phone_number):
    conversation_id = make_conversation(phone_number)
    send_message(conversation_id, "Bug Alert: you are opted in to phone-based notices. Please note that due to limitations with our telephony provider, calls will come from a different phone number, which you should save as a contact: +1 (507) 668-8567. Visit https://bugalert.org/content/pages/my-subscriptions.html to manage notice subscriptions.")

def make_conversation(phone_number):
    url = f"https://{TEXTEMALL_BASE_DOMAIN}/v1/conversations"
    payload={'TextPhoneNumber': '18669481703', 'PhoneNumber': phone_number}
    response = sess.post(url, json=payload)
    print(response.json())
    return response.json().get('ConversationID')

def send_message(conversation_id, msg):
    url = f"https://{TEXTEMALL_BASE_DOMAIN}/v1/conversations/{conversation_id}/textmessages"
    payload={'Message': msg}
    response = sess.post(url, json=payload)
    print(response.json())

def upload_contact_list(category):
    response = table.scan(FilterExpression = Attr(category).contains('e') |Attr(category).contains('s') | Attr(category).contains('p'))
    data = response['Items']

    while 'LastEvaluatedKey' in response:
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        data.extend(response['Items'])

    # TODO tempfile lib!
    with open('/tmp/email.csv', 'w') as email_file, \
         open('/tmp/sms.csv', 'w') as sms_file, \
         open('/tmp/phone.csv', 'w') as phone_file:
        email_file.write("Email\n")
        sms_file.write("First Name,Last Name,Notes,Phone Number\n")
        phone_file.write("First Name,Last Name,Notes,Phone Number\n")
        # https://newbedev.com/using-boto3-in-python-to-acquire-results-from-dynamodb-and-parse-into-a-usable-variable-or-dictionary
        for i in data:
            contact = ast.literal_eval((json.dumps(i)))
            print(contact)
            if 'e' in contact[category]:
                email_file.write(f"{contact.get('email')}\n")
            if 's' in contact[category] and contact.get('phone_country_code') and contact.get('phone_number') and contact.get('phone_country_code') == 1:
                # Text-Em-All seems to need dummy values for name&notes to not flip out
                sms_file.write(f"Bugs,Allert,bugs.allert@example.com,1{contact.get('phone_number')}\n")
            if 'p' in contact[category] and contact.get('phone_country_code') and contact.get('phone_number') and contact.get('phone_country_code') == 1:
                phone_file.write(f"Bugs,Allert,bugs.allert@example.com,1{contact.get('phone_number')}\n")

    # Now put them on telephony services
    email_file_id = upload_email_contacts('/tmp/email.csv')
    sms_file_id = upload_telephony_contacts('/tmp/sms.csv')
    phone_file_id = upload_telephony_contacts('/tmp/phone.csv')
    print(f"email_file_id: {sms_file_id}")
    print(f"sms_file_id: {sms_file_id}")
    print(f"phone_file_id: {phone_file_id}")

    return email_file_id, sms_file_id, phone_file_id

def upload_email_contacts(filepath):
    list_name = datetime.now().strftime("%Y-%m-%d-%H:%M:%S.%f")
    # Create the list
    response = sg.client.marketing.lists.post(
        request_body={"name": list_name}
    )
    list_id = json.loads(response.body).get('id')

    # Create the upload URI
    data = {
        "file_type": "csv",
        "field_mappings": [
            "_rf2_T"
        ],
        "list_ids": [list_id]
    }

    response = sg.client.marketing.contacts.imports.put(
        request_body=data
    )
    print(response.status_code)
    print(response.body)
    print(response.headers)
    response = json.loads(response.body)
    upload_uri = response.get('upload_uri')
    upload_headers = response.get('upload_headers')

    # This respose is terrible and has to be dictionaried
    upload_headers = [{pair.get('header'): pair.get('value')} for pair in upload_headers]

    with open(filepath, 'r') as f:
        payload = f.read()
    print(f"Sending payload: {payload}")

    response = requests.put(upload_uri, headers=upload_headers[0], data=open(filepath,'r').read())
    response.raise_for_status()

    return list_id
    
def upload_telephony_contacts(filepath):
    with open(filepath, 'r') as f:
        payload = f.read()

    print(f"Sending payload: {payload}")
    url = f"https://{TEXTEMALL_BASE_DOMAIN}/v1/fileuploads"
    headers = {
          'Accept': 'application/json',
          'Content-Type': 'text/csv',
    }
    response = sess.post(url, headers=headers, data=payload)
    print (response.json())
    return response.json().get('FileID')
