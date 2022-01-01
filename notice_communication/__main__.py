import logging
import tempfile
import os
import re
import sys
import tweepy
import requests

from google.cloud import texttospeech
from requests_oauthlib import OAuth1Session


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

TEXTEMALL_BASE_DOMAIN = "staging-rest.call-em-all.com"
SUBSCRIPTIONS_API_BASE_DOMAIN = "subscriptions.bugalert.org"
SCRIPT_PATH = os.path.dirname(os.path.realpath(__file__))
os.environ['PATH'] = f"{os.environ['PATH']}:{SCRIPT_PATH}"

def main():
    with open('/tmp/gcp.key', 'w') as f:
        f.write(os.getenv('GCP_KEY'))
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/tmp/gcp.key'

    filename = sys.argv[1]
    summary, category = get_summary_and_category(filename)
    url = f"https://bugalert.org/{filename.replace('md', 'html')}"

    if os.getenv('TWITTER_BEARER_TOKEN'):
        twitter = get_twitter_client()
        tweet = f"{(f'{summary[:220] if len(summary) > 220 else summary)}...'} {url} #BugAlertNotice"
        twitter.create_tweet(text=tweet)

    if os.getenv('TEXT_EM_ALL_ID'):
        send_telephony(summary, category, url, filename)

    print("Operations complete.")

def send_telephony(summary, category, url, filename):
    # Dynamic import to avoid loading up ffmpeg early
    # or unnecessarily.
    from pydub import AudioSegment

    sess = OAuth1Session(os.getenv('TEXT_EM_ALL_ID'),
                         client_secret=os.getenv('TEXT_EM_ALL_SECRET'),
                         resource_owner_key=os.getenv('TEXT_EM_ALL_TOKEN'))

    audio = generate_tts(summary)

    # The response's audio_content is binary.
    with tempfile.NamedTemporaryFile() as out:
        # Write the response to the output file.
        out.write(audio.audio_content)
        intro = AudioSegment.from_mp3(SCRIPT_PATH + "/notice_introduction.mp3")
        notice = AudioSegment.from_mp3(out.name)

    final = intro + notice

    final_filename = os.path.basename(filename) + ".mp3"
    final.export(final_filename, format="mp3")

    if os.getenv('TEXT_EM_ALL_ID'):
        sms_file_id, phone_file_id = update_contact_list(category)
        msg = f"BugAlert: {summary} {url}"
        broadcast = create_sms_broadcast(msg, os.path.basename(filename), sms_file_id, sess)
        print(broadcast)

        audio_id = upload_audio(final_filename, sess)
        broadcast = create_phone_broadcast(audio_id, final_filename, phone_file_id, sess)
        print(broadcast)

def update_contact_list(category):
   headers = {"Origin": "https://bugalert.org"}
   payload = {"category": category,
              "email": "nobody@example.com"} # email field required on API validation rules
   response = requests.post(f"https://{SUBSCRIPTIONS_API_BASE_DOMAIN}/listup", headers=headers, json=payload)
   response.raise_for_status()
   response_dict = response.json()

   return response_dict.get('sms_file_id'), response_dict.get('phone_file_id')

def generate_tts(summary):
    # Instantiates a client
    client = texttospeech.TextToSpeechClient()
    synthesis_input = texttospeech.SynthesisInput(text=f"{summary} The notice will be played once more. {summary}")

    # Build the voice request, select the language code ("en-US")
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        name="en-US-Wavenet-F"
    )

    # Select the type of audio file you want returned
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
        #speaking_rate=0.88
    )

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    return response


def get_summary_and_category(filename):
    f = open(filename, 'r')
    notice = f.read()
    f.close()

    pattern = "Summary: (.*)"
    groups = re.search(pattern, notice)
    summary = groups.group(1)

    pattern = "Category: (.*)"
    groups = re.search(pattern, notice)
    category_verbose = groups.group(1)

    category_keys = {
        "Software Frameworks, Libraries, and Components": "frameworks_libs_components",
        "Operating Systems": "operating_systems",
        "Services & System Applications": "services_system_applications",
        "End-User Applications": "end_user_applications",
        "Test": "test"
    }
    category = category_keys[category_verbose]

    print(summary)
    print(category)

    return summary, category

def upload_audio(filename, sess):
    url = f"https://{TEXTEMALL_BASE_DOMAIN}/v1/audio/{filename}"
    payload={}
    files=[
      ('File',(filename,open(filename,'rb'),'audio/mpeg'))
    ]
    headers = {
      'Accept': 'application/json',
      'Content-Type': 'audio/mpeg',
    }

    response = sess.post(url, headers=headers, data=payload, files=files)
    return response.json()['AudioID']


def create_phone_broadcast(audioid, filename, phone_file_id, sess):
    url = f"https://{TEXTEMALL_BASE_DOMAIN}/v1/broadcasts"
    payload={'BroadcastName': filename, 'BroadcastType': 'Announcement', 'StartDate': '', 'CallerID': '5076688567', 'Audio': {'AudioID': audioid}, 'FileUploads': [{'FileID': phone_file_id}]}
    response = sess.post(url, json=payload)
    return response.json()

def create_sms_broadcast(msg, filename, sms_file_id, sess):
    url = f"https://{TEXTEMALL_BASE_DOMAIN}/v1/broadcasts"
    payload={'BroadcastName': filename, 'BroadcastType': 'SMS', 'StartDate': '', 'TextMessage': msg, 'FileUploads': [{'FileID': sms_file_id}]}
    response = sess.post(url, json=payload)
    return response.json()

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
