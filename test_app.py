import whisper

model = whisper.load_model("medium.en")
transcription = model.transcribe("preamble.wav")['text']
print(transcription)