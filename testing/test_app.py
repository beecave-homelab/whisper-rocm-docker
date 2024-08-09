import whisper
import urllib.request
import os
from dotenv import load_dotenv
from 

# Load environment variables from .env file
load_dotenv()

# Get variables from .env file and assign them to constants
MODEL = os.getenv("MODEL", "medium.en")
MODEL_DIR = os.getenv("MODEL_DIR", "./whisper-model/")
WAV_FILE_URL = os.getenv("WAV_FILE_URL")
FILE_UPLOAD_DIRECTORY = os.getenv("FILE_UPLOAD_DIRECTORY", "./uploads/")

# Define the path for the WAV file
WAV_FILE_PATH = os.path.join(FILE_UPLOAD_DIRECTORY, "preamble.wav")

# Ensure the directory exists
os.makedirs(FILE_UPLOAD_DIRECTORY, exist_ok=True)

try:
    # Download the .wav file
    urllib.request.urlretrieve(WAV_FILE_URL, WAV_FILE_PATH)
    print(f"Downloaded .wav file to {WAV_FILE_PATH}")
    
    # Load the Whisper model and specify the custom model directory
    model = whisper.load_model(MODEL, download_root=MODEL_DIR)

    # Perform transcription
    transcription = model.transcribe(WAV_FILE_PATH)['text']

    # Print the transcription
    print(transcription)

except Exception as e:
    print(f"An error occurred: {e}")