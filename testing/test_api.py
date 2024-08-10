import whisper
import urllib.request
import os
import threading
import time
from flask import Flask, abort, request
from tempfile import NamedTemporaryFile
from modules.whisper_integration import transcribe_audio
from dotenv import load_dotenv
import logging

# Load environment variables from .env file
load_dotenv()

# Setup logging
logging.basicConfig(level=logging.INFO)

# Environment variables with error handling
try:
    MODEL_NAME = os.getenv("MODEL_NAME", "base")
    TEMPERATURE = float(os.getenv("TEMPERATURE", 0.7))
    PORT = int(os.getenv("PORT", 5000))
    TIMEOUT_DURATION = int(os.getenv("TIMEOUT_DURATION", 600))  # Default to 600 seconds (10 minutes)
except ValueError as e:
    raise ValueError("Invalid environment variable configuration") from e

app = Flask(__name__)

# Global variables to manage model and timeout
model = None
last_request_time = None

# Function to load the model
def load_model():
    global model
    if model is None:
        logging.info(f"Loading Whisper model: {MODEL_NAME}")
        model = whisper.load_model(MODEL_NAME)
    return model

# Function to unload the model
def unload_model():
    global model
    if model is not None:
        logging.info("Unloading Whisper model due to inactivity")
        model = None

# Function to track the last request time and unload the model if timeout occurs
def track_inactivity():
    global last_request_time
    while True:
        if last_request_time and (time.time() - last_request_time) > TIMEOUT_DURATION:
            unload_model()
            last_request_time = None
        time.sleep(60)  # Check every minute

# Start the inactivity tracking thread
inactivity_thread = threading.Thread(target=track_inactivity, daemon=True)
inactivity_thread.start()

@app.route('/v1/audio/transcriptions', methods=['POST'])
def handler():
    global last_request_time
    last_request_time = time.time()

    if not request.files:
        abort(400)

    results = []

    for filename, handle in request.files.items():
        if handle.mimetype not in ['audio/wav', 'audio/mpeg']:
            abort(400, description="Unsupported file type")
        
        with NamedTemporaryFile() as temp:
            handle.save(temp)
            model_instance = load_model()  # Load model if not already loaded
            transcript = model_instance.transcribe(temp.name)
            results.append({
                'filename': filename,
                'transcript': transcript,
            })

    return {'results': results}

if __name__ == "__main__":
    logging.info(f"Starting server on port {PORT}")
    app.run(host='0.0.0.0', port=PORT, debug=True)