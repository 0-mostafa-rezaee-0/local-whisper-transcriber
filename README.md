<h1 align="center">Whisper Docker Transcriber</h1>

<h2 align="center">Transcribe Audio Files in 30 Seconds</h2>

**The easiest way to transcribe audio files using AI.** Just drag, drop, and get your transcript.

## Table of Contents

1. [Ultra-Quick Start (One Command)](#1-ultra-quick-start-one-command)
2. [Dev Container (VS Code/Cursor)](#2-dev-container-vs-codecursor)
3. [Quick Start (3 Steps)](#3-quick-start-3-steps)
   - [Option A: Web Interface (Easiest)](#option-a-web-interface-easiest)
   - [Option B: API Interface](#option-b-api-interface)
4. [Supported Formats](#4-supported-formats)
5. [Command Line (Alternative)](#5-command-line-alternative)
6. [Why This Tool?](#6-why-this-tool)
7. [Contributing](#7-contributing)
8. [License](#8-license)

## 1. Ultra-Quick Start (One Command)

**The absolute easiest way - just run one command:**

```bash
./start.sh
```

### What happens when you run this command:

1. **System Check** (5 seconds)
   - ✅ Checks if Docker is installed and running
   - ✅ Detects if you have NVIDIA GPU for faster processing
   - ✅ Shows colored status messages

2. **Automatic Setup** (2-5 minutes)
   - ✅ Downloads and builds the Docker image automatically
   - ✅ Installs all dependencies (Whisper, CUDA, etc.)
   - ✅ No manual configuration needed

3. **Choose Your Interface**
   - **Option 1**: Web Interface (Drag & Drop) - Opens browser automatically
   - **Option 2**: API Interface (For developers) - Opens API docs
   - **Option 3**: Command Line - Shows usage examples

4. **Start Transcribing** (30 seconds)
   - ✅ Browser opens automatically to the interface
   - ✅ Upload your audio file (MP3, WAV, etc.)
   - ✅ Get instant transcription
   - ✅ Download results in any format

### Prerequisites (one-time setup):
- **Docker** installed on your system
- **NVIDIA GPU** (optional, but recommended for speed)

### Example workflow:
```bash
# 1. Run the setup
./start.sh

# 2. Choose "1" for web interface
# 3. Browser opens to http://localhost:8501
# 4. Drag your audio file
# 5. Get your transcript in 30 seconds!
```

## 2. Dev Container (VS Code/Cursor)

**For developers - even easier:**

### What happens:
1. **Open in IDE**: Open this repo in **Cursor** or **VS Code**
2. **Auto-detection**: IDE detects `.devcontainer` folder and shows "Reopen in Container" button
3. **Automatic setup**: Container builds automatically with all dependencies
4. **Ready to use**: Run `make start-web` or `make start-api`
5. **Auto-cleanup**: Container stops when you close the IDE

### Benefits:
- ✅ **Zero Docker knowledge needed** - IDE handles everything
- ✅ **Automatic GPU detection** - Works with your hardware
- ✅ **Full development environment** - Python, extensions, everything ready
- ✅ **Automatic cleanup** - No leftover containers
- ✅ **Port forwarding** - Web interfaces work automatically

### Example workflow:
```bash
# 1. Open repo in Cursor/VS Code
# 2. Click "Reopen in Container" 
# 3. Wait 2-3 minutes for setup
# 4. Run: make start-web
# 5. Browser opens to http://localhost:8501
# 6. Start transcribing!
```

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

## 6. Why This Tool?
- **Fast**: GPU-accelerated with CUDA support
- **Accurate**: Uses OpenAI's Whisper large-v3 model
- **Easy**: Web interface + simple CLI
- **Flexible**: Multiple output formats

## 7. Contributing
Found a bug? Have an idea? [Open an issue](https://github.com/yourusername/whisper-docker-transcriber/issues) or submit a PR!


