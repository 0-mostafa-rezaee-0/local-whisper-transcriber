# Examples Directory

This directory contains sample audio files and usage examples for the Whisper Docker Transcriber.

## Contents

- `sample_audio.mp3` - Example audio file for testing transcription
- Additional sample files can be added here for demonstration purposes

## Usage

To test the transcriber with sample audio:

```bash
# Using Docker
docker run --gpus all -v $(pwd):/app whisper-transcriber /app/examples/sample_audio.mp3

# Using local Python
python app.py examples/sample_audio.mp3
```

## Adding Your Own Audio Files

Place your audio files in this directory and reference them in your transcription commands. Supported formats include:

- MP3
- WAV  
- M4A
- FLAC
- OGG
- AAC

## Note

Audio files in this directory are ignored by git (see `.gitignore`) to keep the repository size manageable. Add your own test files as needed.
