import whisper
import os
from dotenv import load_dotenv

load_dotenv()

MODEL_NAME = os.getenv("MODEL_NAME")
TEMPERATURE = float(os.getenv("TEMPERATURE", 0.7))

def transcribe_audio(file_path):
    model = whisper.load_model(MODEL_NAME)
    result = model.transcribe(file_path, temperature=TEMPERATURE)
    return result['text']