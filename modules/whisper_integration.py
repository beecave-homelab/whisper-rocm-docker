import whisper
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

MODEL_NAME = os.getenv("MODEL_NAME", "base")
TEMPERATURE = float(os.getenv("TEMPERATURE", 0.7))

# Load the Whisper model
model = whisper.load_model(MODEL_NAME)

def transcribe_audio(file_path):
    result = model.transcribe(file_path, temperature=TEMPERATURE)
    return result['text']