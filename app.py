import gradio as gr
from modules.whisper_integration import transcribe_audio

def transcribe(file):
    return transcribe_audio(file.name)

iface = gr.Interface(
    fn=transcribe,
    inputs=gr.Audio(source="upload", type="filepath"),
    outputs="text",
    title="Whisper Speech-to-Text",
    description="Upload an audio file to transcribe it to text using OpenAI's Whisper model."
)

if __name__ == "__main__":
    iface.launch()