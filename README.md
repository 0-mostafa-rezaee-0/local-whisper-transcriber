# Whisper Docker Transcriber

<h1 align="center">🎤 Transcribe Audio Files in 30 Seconds</h1>

**The easiest way to transcribe audio files using AI.** Just drag, drop, and get your transcript.

## 🚀 Quick Start (3 Steps)

### Option A: Web Interface (Easiest)
```bash
# Build & Run Streamlit app
docker build -t whisper-transcriber .
docker run --gpus all -p 8501:8501 -v $(pwd):/app whisper-transcriber streamlit run scripts/web_app.py --server.port=8501 --server.address=0.0.0.0
```
Visit: `http://localhost:8501` → Drag, drop, transcribe! 🎉

### Option B: API Interface
```bash
# Build & Run API
docker build -t whisper-transcriber .
docker run --gpus all -p 8000:8000 -v $(pwd):/app whisper-transcriber python scripts/app.py /app/audio.mp3 --api
```
Visit: `http://localhost:8000/docs` → Upload via API

**That's it!** 🎉

## 📁 Supported Formats
**Audio**: MP3, WAV, M4A, FLAC, OGG, AAC  
**Output**: Text, JSON, SRT subtitles

## 🖥️ Command Line (Alternative)
```bash
# Simple transcription
python scripts/app.py your_audio.mp3

# With options
python scripts/app.py your_audio.mp3 --model large-v2 --output-format srt
```

## 📚 Need More Details?
- [Full Documentation](docs/README.md)
- [API Reference](docs/API.md)
- [Troubleshooting](docs/TROUBLESHOOTING.md)
- [Advanced Usage](docs/ADVANCED.md)

## ⚡ Why This Tool?
- **Fast**: GPU-accelerated with CUDA support
- **Accurate**: Uses OpenAI's Whisper large-v3 model
- **Easy**: Web interface + simple CLI
- **Flexible**: Multiple output formats

## 🤝 Contributing
Found a bug? Have an idea? [Open an issue](https://github.com/yourusername/whisper-docker-transcriber/issues) or submit a PR!

## 📄 License
MIT License - see [LICENSE](LICENSE) file for details.

---
**Made with ❤️ for easy audio transcription**