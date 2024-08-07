Whisper on an AMD GPU with rocm

# whisper-rocm-docker

This project provides a Gradio web UI for interacting with OpenAI's Whisper model to convert speech to text. The Whisper model is downloaded and run locally, and the application is configured using environment variables.

## Project Structure

```plaintext
/project_root
    /app
        __init__.py
        app.py
    /modules
        __init__.py
        whisper_integration.py
    .env
    .env.example
    requirements.txt
    README.md
```

## Description

This project sets up a web interface using Gradio to transcribe audio files into text using the Whisper model. The model is configured to run locally, and the transcription can be customized using environment variables.

## Installation

1. **Clone the repository**

    ```bash
    git clone https://github.com/beecave-homelab/whisper-rocm-docker.git
    cd whisper-rocm-docker
    ```

2. **Create a virtual environment and activate it**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Install `ffmpeg`**

    On Ubuntu, run:

    ```bash
    sudo apt update && sudo apt install ffmpeg
    ```

5. **Copy `.env.example` to `.env`**

    ```bash
    cp .env.example .env
    ```

6. **Configure the environment variables in `.env`**

    ```plaintext
    MODEL_NAME=medium.en
    TEMPERATURE=0.7
    ```

## Usage

To run the application, execute the following command:

```bash
python3 app.py
```

This will launch the Gradio web interface, where you can upload an audio file to transcribe it to text using OpenAI's Whisper model.

## License

This project is licensed under the MIT license. See [LICENSE](LICENSE) for more information.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Badges

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Gradio](https://img.shields.io/badge/Gradio-3.x-blue)
![OpenAI Whisper](https://img.shields.io/badge/OpenAI_Whisper-medium.en-blue)
![License](https://img.shields.io/badge/License-MIT-blue)

## Environment Variables

The application uses the following environment variables which are configured in the `.env` file:

- `MODEL_NAME`: The name of the Whisper model to use (e.g., `medium.en`).
- `TEMPERATURE`: The temperature setting for the Whisper model.

## Author

Elvee

---

For more information on how to use the Whisper model with Hugging Face or OpenAI's official code release, please refer to the guide provided in the project documentation.