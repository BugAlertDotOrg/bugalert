import logging
import tempfile
import os
import re
import requests
import sys

from google.cloud import texttospeech


os.environ['PATH'] = os.environ['PATH'] + ':/tmp'
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

GCP_KEY = os.getenv('GCP_KEY')
with open('/tmp/gcp.key', 'w') as f:
    f.write(GCP_KEY)
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/tmp/gcp.key'


#r = requests.get("https://bubblesoftapps.com/bubbleupnpserver/ffmpeg_binaries/linux/amd64/ffmpeg")
#with open('/tmp/ffmpeg', 'wb') as f:
#    f.write(r.content)
#os.chmod('/tmp/ffmpeg', 0o755)

#r = requests.get("https://bubblesoftapps.com/bubbleupnpserver/ffmpeg_binaries/linux/amd64/ffprobe")
#with open('/tmp/ffprobe', 'wb') as f:
#    f.write(r.content)
#os.chmod('/tmp/ffprobe', 0o755)

from pydub import AudioSegment

def main():
    filename = sys.argv[1]
    #r = requests.get("https://raw.githubusercontent.com/sullivanmatt/bugalert/main/%s" % filename)
    #notice = r.text
    #print(notice)
    f = open(filename, 'r')
    notice = f.read()
    f.close()

    pattern = "Summary:(.*)"
    groups = re.search(pattern, notice)
    summary = groups.group(0)
    print(summary)

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

    # The response's audio_content is binary.
    with tempfile.NamedTemporaryFile() as out:
        # Write the response to the output file.
        out.write(response.audio_content)
        intro = AudioSegment.from_mp3("notice_introduction.mp3")
        notice = AudioSegment.from_mp3(out.name)

        final = intro + notice
        final.export(out.name + ".final.mp3", format="mp3")
        print(out.name + ".final.mp3")


if __name__ == '__main__':
    main()
