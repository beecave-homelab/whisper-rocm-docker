from flask import Flask, abort, request
from tempfile import NamedTemporaryFile
from modules.whisper_integration import transcribe_audio
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Environment variables
MODEL_NAME = os.getenv("MODEL_NAME", "base")
TEMPERATURE = float(os.getenv("TEMPERATURE", 0.7))
PORT = int(os.getenv("PORT", 5000))

app = Flask(__name__)

@app.route('/v1/audio/transcriptions', methods=['POST'])
def handler():
    if not request.files:
        # If the user didn't submit any files, return a 400 (Bad Request) error.
        abort(400)

    # For each file, let's store the results in a list of dictionaries.
    results = []

    # Loop over every file that the user submitted.
    for filename, handle in request.files.items():
        # Create a temporary file.
        # The location of the temporary file is available in `temp.name`.
        temp = NamedTemporaryFile()
        # Write the user's uploaded file to the temporary file.
        # The file will get deleted when it drops out of scope.
        handle.save(temp)
        # Let's get the transcript of the temporary file.
        transcript = transcribe_audio(temp.name)
        # Now we can store the result object for this file.
        results.append({
            'filename': filename,
            'transcript': transcript,
        })

    # This will be automatically converted to JSON.
    return {'results': results}

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=PORT, debug=True)


# TO DO
# - Add support for all functionality named in this guide: https://platform.openai.com/docs/api-reference/audio/createTranscription
# - Add support for all functionality named in this guide: https://platform.openai.com/docs/api-reference/audio/createTranslation