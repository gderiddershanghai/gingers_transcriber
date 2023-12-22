import requests
import assemblyai as aai
import os
from dotenv import load_dotenv, find_dotenv

# Load API key from .env file
_ = load_dotenv(find_dotenv())
aai.settings.api_key = os.getenv('ASSEMBLYAI_API_KEY')

def transcribe_video(fp):
    try:
        transcriber = aai.Transcriber()
        print('----------')
        print(transcriber)
        transcript = transcriber.transcribe(fp)

        try:
            with open('transcript.txt', 'w') as file:
                file.write(transcript)
                print("Transcript saved as 'transcript.txt'.")
        except IOError:
            print("Error: File cannot be opened or written to.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
# transcribe_video('path_to_your_video_file')
