# Whisper Docker Transcriber

<h1 align="center">Transcribe Audio Files in 30 Seconds</h1>

**The easiest way to transcribe audio files using AI.** Just drag, drop, and get your transcript.

## Table of Contents

1. [Ultra-Quick Start (One Command)](#1-ultra-quick-start-one-command)
2. [Dev Container (VS Code/Cursor)](#2-dev-container-vs-codecursor)
3. [Quick Start (3 Steps)](#3-quick-start-3-steps)
   - [Option A: Web Interface (Easiest)](#option-a-web-interface-easiest)
   - [Option B: API Interface](#option-b-api-interface)
4. [Supported Formats](#4-supported-formats)
5. [Command Line (Alternative)](#5-command-line-alternative)
6. [Need More Details?](#6-need-more-details)
7. [Why This Tool?](#7-why-this-tool)
8. [Contributing](#8-contributing)
9. [License](#9-license)

## 1. Ultra-Quick Start (One Command)

**The absolute easiest way - just run one command:**

```bash
./start.sh
```

That's it! The script will:
- ✅ Check your system (Docker, GPU)
- ✅ Build the Docker image automatically
- ✅ Ask which interface you want (Web/API/CLI)
- ✅ Start everything and open your browser
- ✅ Handle all the complexity for you

## 2. Dev Container (VS Code/Cursor)

**For developers - even easier:**

1. Open this repo in **Cursor** or **VS Code**
2. Click **"Reopen in Container"** when prompted
3. Wait for container to start
4. Run `make start-web` or `make start-api`
5. Done! 🎉

**Benefits:**
- ✅ No Docker knowledge needed
- ✅ Automatic GPU detection
- ✅ Container stops when you close Cursor
- ✅ Full development environment ready

## 3. Quick Start (3 Steps)

### Option A: Web Interface (Easiest)
```bash
# Build & Run Streamlit app
docker build -t whisper-transcriber .
docker run --gpus all -p 8501:8501 -v $(pwd):/app whisper-transcriber streamlit run scripts/web_app.py --server.port=8501 --server.address=0.0.0.0
```
Visit: `http://localhost:8501` → Drag, drop, transcribe!

### Option B: API Interface
```bash
# Build & Run API
docker build -t whisper-transcriber .
docker run --gpus all -p 8000:8000 -v $(pwd):/app whisper-transcriber python scripts/app.py /app/audio.mp3 --api
```
Visit: `http://localhost:8000/docs` → Upload via API

**That's it!**

### Alternative: Docker Compose
```bash
# Start web interface
make start-web

# Start API interface  
make start-api

# Stop everything
make stop
```

## 4. Supported Formats
**Audio**: MP3, WAV, M4A, FLAC, OGG, AAC  
**Output**: Text, JSON, SRT subtitles

## 5. Command Line (Alternative)
```bash
# Simple transcription
python scripts/app.py your_audio.mp3

# With options
python scripts/app.py your_audio.mp3 --model large-v2 --output-format srt
```

## 6. Need More Details?
- [Full Documentation](docs/README.md)
- [API Reference](docs/API.md)
- [Troubleshooting](docs/TROUBLESHOOTING.md)
- [Advanced Usage](docs/ADVANCED.md)

## 7. Why This Tool?
- **Fast**: GPU-accelerated with CUDA support
- **Accurate**: Uses OpenAI's Whisper large-v3 model
- **Easy**: Web interface + simple CLI
- **Flexible**: Multiple output formats

## 8. Contributing
Found a bug? Have an idea? [Open an issue](https://github.com/yourusername/whisper-docker-transcriber/issues) or submit a PR!

## 9. License
MIT License - see [LICENSE](LICENSE) file for details.

---
**Made with love for easy audio transcription**