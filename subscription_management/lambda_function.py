import logging
import os
import sys
import codecs
import hashlib
import hmac
import base64
import boto3

import simplejson as json
from requests_oauthlib import OAuth1Session
from boto3.dynamodb.conditions import Key
from email_validator import validate_email, EmailNotValidError

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

dynamo = boto3.resource('dynamodb')
ses = boto3.client('ses', region_name="us-east-1")
hmacsecret = os.getenv('HMACSECRET')
hmacsecret = codecs.encode(hmacsecret)

TEXTEMALL_BASE_DOMAIN = "staging-rest.call-em-all.com"


def respond_error(err, origin, status=400):
    return {
        'statusCode': status,
        'body': "{\"error\": \"%s\"}" % err,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': origin,
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Expose-Headers': 'Content-Type',
            'Access-Control-Allow-Methods': 'GET, POST, OPTIONS, HEAD'
        },
    }

def respond_success(msg, origin):
    return {
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

def lambda_handler(event, context):
    headers = event.get('headers')
    headers = {k.lower():v for k,v in headers.items()}
    logger.info("%s %s %s %s %s %s" % (headers.get('x-forwarded-for', 'no-ip'), event.get('httpMethod', 'no-method'), event.get('path', 'no-path'), headers.get('user-agent', 'no-ua'), headers.get('referer', 'no-referer'), headers.get('origin', 'no-origin')))
    method = event.get('httpMethod')
    origin = headers.get('origin')
    table = dynamo.Table('bugalert-subscriptions-prod')

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

    if method == 'POST' and path == 'verify':
        # Fire off email
        locally_computed_hmac = hmac.new(hmacsecret, codecs.encode(email), hashlib.sha256).digest()
        signature = base64.urlsafe_b64encode(locally_computed_hmac).decode('utf8').rstrip("=")
        msg_body = "Please visit the following URL to verify your email address: " \
                   "https://bugalert.org/content/pages/my-subscriptions.html" \
                   "?signature={}&email={}".format(signature, email)
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

        response = table.update_item(
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

        return respond_success("{\"status\": \"success\"}", origin)

    return respond_error("Unsupported method %s" % method, origin, status=405)

    #print(vars(event))
    #print(vars(context))

    #sess = OAuth1Session(os.getenv('TEXT_EM_ALL_ID'),
    #                     client_secret=os.getenv('TEXT_EM_ALL_SECRET'),
    #                     resource_owner_key=os.getenv('TEXT_EM_ALL_TOKEN'))


def add_contact(sess):
    url = "https://%s/v1/broadcasts" % TEXTEMALL_BASE_DOMAIN
    payload={'BroadcastName': filename, 'BroadcastType': 'Announcement', 'StartDate': '', 'CallerID': '5076688567', 'Audio': {'AudioID': audioid}, 'Lists': [{'ListID': '2'}]}
    response = sess.post(url, json=payload)
    return response.json()
