import logging
import tempfile
import os
import re
import sys
import tweepy
import requests
import datetime
import json

from email_content import html_template
from sendgrid import SendGridAPIClient

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

SUBSCRIPTIONS_API_BASE_DOMAIN = "subscriptions.bugalert.org"

def main():
    filename = sys.argv[1]
    summary, category, title, slug, tags = get_content_meta(filename)
    url = f"https://bugalert.org/{filename.replace('md', 'html')}"
    if os.getenv('TWITTER_BEARER_TOKEN') and category != "dev":
        twitter = get_twitter_client()
        tweet_summary = summary[:220] if len(summary) > 220 else summary
        ellipsis = "..." if len(summary) > 220 else ""
        hashtag = "#BugAlertNews" if category == "bug_alert_news" else "#BugAlertNotice"
        tweet = f"{f'{tweet_summary}{ellipsis}'} {url}?src=tw {hashtag}"
        twitter.create_tweet(text=tweet)

    if category == "bug_alert_news":
        return

    # Send Telegram
    if os.getenv('TELEGRAM_API_KEY') and category != "dev" and category != "test":
        send_telegram(summary, category, title, url)

    if os.getenv('SENDGRID_API_KEY'):
        email_file_id  = update_contact_list(category)
        create_email_broadcast(summary, category, title, url, slug, os.path.basename(filename), email_file_id)

    if os.getenv('API_KEY'):
        send_telephony_twilio(summary, category, title, tags, url, filename)

    print("Operations complete.")

def send_telegram(summary, category, title, url):
    TELEGRAM_API_KEY = os.getenv('TELEGRAM_API_KEY')
    TG_CHAT_ID = "@BugAlert"
    msg = f"{title}: {summary}\n{url}?src=tg"
    url_to_send = f"https://api.telegram.org/bot{TELEGRAM_API_KEY}/sendMessage?chat_id={TG_CHAT_ID}&text={msg}"
    response = requests.get(url_to_send)
    response.raise_for_status()
    print(response.json())

def send_telephony_twilio(summary, category, title, tags, url, filename):
    msg = f"Bug Alert: {summary} {url}?src=s"
    create_sms_broadcast_to_twilio(category, msg)

    # Only phone call for critical severity
    if 'critical severity' in tags.lower() or category == 'dev':
        create_phone_broadcast_to_twilio(category, msg)

def update_contact_list(category):
    headers = {"Origin": "https://bugalert.org"}
    payload = {"category": category,
                "email": "nobody@example.com",
                "api_key": os.getenv('API_KEY')} # email field required on API validation rules
    response = requests.post(f"https://{SUBSCRIPTIONS_API_BASE_DOMAIN}/listup", headers=headers, json=payload)
    response.raise_for_status()
    response_dict = response.json()

    return response_dict.get('email_file_id')

def get_content_meta(filename):
    with open(filename, 'r') as f:
        notice = f.read()

    pattern = "Summary: (.*)"
    groups = re.search(pattern, notice)
    summary = groups.group(1)

    pattern = "Title: (.*)"
    groups = re.search(pattern, notice)
    title = groups.group(1)

    pattern = "Category: (.*)"
    groups = re.search(pattern, notice)
    category_verbose = groups.group(1)

    pattern = "Slug: (.*)"
    groups = re.search(pattern, notice)
    slug = groups.group(1)

    pattern = "Tags: (.*)"
    groups = re.search(pattern, notice)
    tags = groups.group(1)

    category_keys = {
        "Software Frameworks, Libraries, and Components": "frameworks_libs_components",
        "Operating Systems": "operating_systems",
        "Services & System Applications": "services_system_applications",
        "End-User Applications": "end_user_applications",
        "Test": "test",
        "Dev": "dev",
        "Bug Alert News": "bug_alert_news"
    }
    category = category_keys[category_verbose]

    print(summary)
    print(title)
    print(category)
    print(slug)
    print(tags)

    return summary, category, title, slug, tags

def create_sms_broadcast_to_twilio(category, msg):
    headers = {"Origin": "https://bugalert.org"}
    payload = {"category": category,
                "email": "nobody@example.com",
                "message": msg,
                "api_key": os.getenv('API_KEY')} # email field required on API validation rules
    response = requests.post(f"https://{SUBSCRIPTIONS_API_BASE_DOMAIN}/runsms", headers=headers, json=payload)
    response_dict = response.json()

    print(response_dict)

def create_phone_broadcast_to_twilio(category, msg):
    headers = {"Origin": "https://bugalert.org"}
    payload = {"category": category,
                "email": "nobody@example.com",
                "message": msg,
                "api_key": os.getenv('API_KEY')} # email field required on API validation rules
    response = requests.post(f"https://{SUBSCRIPTIONS_API_BASE_DOMAIN}/runtel", headers=headers, json=payload)
    response_dict = response.json()

    print(response_dict)

def create_email_broadcast(summary, category, title, url, slug, filename, email_file_id):
    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))

    # Give SendGrid a bit to process the contact list additions
    send_date = datetime.datetime.utcnow() + datetime.timedelta(minutes=6)
    send_date = send_date.replace(microsecond=0).isoformat() + "Z"
    url = url + '?src=e'
    data = {
        "name": f"{filename}-{send_date}",
        "send_at": send_date,
        "send_to": { "list_ids": [email_file_id] },
        "email_config": {
            "subject": f"Bug Alert Notice: {title}",
            "generate_plain_content": True,
            "html_content": html_template.replace("{title}", title).replace("{summary}", summary).replace("{url}", url).replace("{slug}", slug),
            "custom_unsubscribe_url": "https://bugalert.org/content/pages/my-subscriptions.html",
            "sender_id": 2415793
        }
    }

    response = sg.client.marketing.singlesends.post(
        request_body=data
    )
    single_send_id = json.loads(response.body).get('id')

    # Signal to the campaign that everything is final and ready to ship
    response = sg.client.marketing.singlesends._(single_send_id).schedule.put(
        request_body={"send_at": send_date}
    )

def get_twitter_client():
    api = tweepy.Client(
        bearer_token=os.getenv('TWITTER_BEARER_TOKEN'),
        consumer_key=os.getenv('TWITTER_CONSUMER_KEY'),
        consumer_secret=os.getenv('TWITTER_CONSUMER_SECRET'),
        access_token=os.getenv('TWITTER_ACCESS_TOKEN'),
        access_token_secret=os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
    )
    return api

if __name__ == '__main__':
    main()
