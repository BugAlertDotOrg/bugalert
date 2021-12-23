import logging
import tempfile
import os
import re
import requests
import sys

from google.cloud import texttospeech
from requests_oauthlib import OAuth1Session


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

TEXTEMALL_BASE_DOMAIN = "staging-rest.call-em-all.com"
SCRIPT_PATH = os.path.dirname(os.path.realpath(__file__))

sess = OAuth1Session(os.getenv('TEXT_EM_ALL_ID'),
                      client_secret=os.getenv('TEXT_EM_ALL_SECRET'),
                      resource_owner_key=os.getenv('TEXT_EM_ALL_TOKEN'))
os.environ['PATH'] = "%s:%s" % (os.environ['PATH'], SCRIPT_PATH)
from pydub import AudioSegment

def main():
    with open('/tmp/gcp.key', 'w') as f:
        f.write(os.getenv('GCP_KEY'))
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/tmp/gcp.key'

    summary = get_summary()
    audio = generate_tts(summary)

    # The response's audio_content is binary.
    with tempfile.NamedTemporaryFile() as out:
        # Write the response to the output file.
        out.write(audio.audio_content)
        intro = AudioSegment.from_mp3(SCRIPT_PATH + "/notice_introduction.mp3")
        notice = AudioSegment.from_mp3(out.name)

    final = intro + notice

    final_filename = os.path.basename(sys.argv[1]) + ".mp3"
    final.export(final_filename, format="mp3")
    print(final_filename)

    audio_id = upload_audio(final_filename)
    print(audio_id)

    broadcast = create_broadcast(audio_id, final_filename)
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


def get_summary():
    filename = sys.argv[1]
    f = open(filename, 'r')
    notice = f.read()
    f.close()

    pattern = "Summary: (.*)"
    groups = re.search(pattern, notice)
    summary = groups.group(1)
    print(summary)

    return summary

def upload_audio(filename):
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

def create_broadcast(audioid, filename):
    url = "https://%s/v1/broadcasts" % TEXTEMALL_BASE_DOMAIN
    payload={'BroadcastName': filename, 'BroadcastType': 'Announcement', 'StartDate': '', 'CallerID': '5076688567', 'Audio': {'AudioID': audioid}, 'Lists': [{'ListID': '2'}]}
    response = sess.post(url, json=payload)
    return response.json()


if __name__ == '__main__':
    main()
