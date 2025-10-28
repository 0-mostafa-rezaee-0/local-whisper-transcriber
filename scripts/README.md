# Scripts Directory

This directory contains the main Python scripts for the Whisper Docker Transcriber.

## Contents

- `app.py` - Main application with CLI and FastAPI interfaces

## Usage

The main script can be run directly:

```bash
# CLI mode
python scripts/app.py audio.mp3

# API mode
python scripts/app.py audio.mp3 --api

# With options
python scripts/app.py audio.mp3 --model large-v2 --output-format json
```

## Script Features

- GPU-accelerated transcription using faster-whisper
- Command-line interface with comprehensive options
- Optional FastAPI web service
- Multiple output formats (text, JSON, SRT)
- Configurable model sizes and compute types
