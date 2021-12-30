import logging
import tempfile
import os
import re
import sys
import tweepy

from google.cloud import texttospeech
from requests_oauthlib import OAuth1Session


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
os.environ['PATH'] = "%s:%s" % (os.environ['PATH'], SCRIPT_PATH)

TEXTEMALL_BASE_DOMAIN = "staging-rest.call-em-all.com"
SCRIPT_PATH = os.path.dirname(os.path.realpath(__file__))

def main():
    with open('/tmp/gcp.key', 'w') as f:
        f.write(os.getenv('GCP_KEY'))
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/tmp/gcp.key'

    filename = sys.argv[1]
    summary = get_summary(filename)

    if os.getenv('TWITTER_BEARER_TOKEN'):
        twitter = get_twitter_client()
        url = "https://bugalert.org/%s" % filename.replace('md', 'html')
        tweet = "%s %s #BugAlertNotice" % (("%s..." % summary[:220] if len(summary) > 220 else summary), url)
        twitter.create_tweet(text=tweet)

    if os.getenv('TEXT_EM_ALL_ID'):
        send_telephony(summary, filename)

def send_telephony(summary, filename)
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
    print(final_filename)

    if os.getenv('TEXT_EM_ALL_ID'):
        audio_id = upload_audio(final_filename, sess)
        print(audio_id)

        broadcast = create_broadcast(audio_id, final_filename, sess)
        print(broadcast)

def generate_tts(summary):
    # Instantiates a client
    client = texttospeech.TextToSpeechClient()
    synthesis_input = texttospeech.SynthesisInput(text="%s The notice will be played once more. %s" % (summary, summary))

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


def get_summary(filename):
    f = open(filename, 'r')
    notice = f.read()
    f.close()

    pattern = "Summary: (.*)"
    groups = re.search(pattern, notice)
    summary = groups.group(1)
    print(summary)

    return summary

def upload_audio(filename, sess):
    url = "https://%s/v1/audio/%s" % (TEXTEMALL_BASE_DOMAIN, filename)
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

def create_broadcast(audioid, filename, sess):
    url = "https://%s/v1/broadcasts" % TEXTEMALL_BASE_DOMAIN
    payload={'BroadcastName': filename, 'BroadcastType': 'Announcement', 'StartDate': '', 'CallerID': '5076688567', 'Audio': {'AudioID': audioid}, 'Lists': [{'ListID': '2'}]}
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
