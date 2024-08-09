import whisper
import urllib.request
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get variables from .env file and assign them to constants
MODEL_DIR = os.getenv("MODEL_DIR")
WAV_FILE = os.getenv("WAV_FILE")
FILE_UPLOAD_DIRECTORY = os.getenv("FILE_UPLOAD_DIRECTORY")

# Define the path for the WAV file
WAV_FILE_PATH = os.path.join(FILE_UPLOAD_DIRECTORY, "preamble.wav")

# Ensure the directory exists
os.makedirs(FILE_UPLOAD_DIRECTORY, exist_ok=True)

# Download the .wav file
urllib.request.urlretrieve(WAV_FILE, WAV_FILE_PATH)
print(f"Downloaded .wav file to {WAV_FILE_PATH}")

# Load the Whisper model and specify the custom model directory
model = whisper.load_model("medium.en", download_root=MODEL_DIR)

# Perform transcription
transcription = model.transcribe(WAV_FILE_PATH)['text']

# Print the transcription
print(transcription)