# Whisper Docker Transcriber

<h1 align="center">🎤 GPU-Accelerated Audio Transcription</h1>

A production-ready Docker container for high-performance audio transcription using OpenAI's Whisper model with GPU acceleration. Built with `faster-whisper` for optimal speed and memory efficiency.

## ✨ Features

- **🚀 GPU Acceleration**: CUDA support for lightning-fast transcription
- **📦 Docker Ready**: One-command deployment with Docker
- **🎯 Multiple Models**: Support for all Whisper model sizes (tiny to large-v3)
- **🌐 API & CLI**: Both command-line interface and FastAPI web service
- **📝 Multiple Formats**: Output in text, JSON, or SRT subtitle format
- **⚡ Optimized**: Uses `faster-whisper` for 2-4x speed improvement
- **🔧 Flexible**: Configurable compute types and device selection

## 🚀 Quick Start

### Prerequisites

- Docker with GPU support (NVIDIA Container Toolkit)
- NVIDIA GPU with CUDA support
- At least 4GB GPU memory (for large models)

### 1. Clone and Build

```bash
git clone https://github.com/yourusername/whisper-docker-transcriber.git
cd whisper-docker-transcriber
docker build -t whisper-transcriber .
```

### 2. Basic Usage

```bash
# Transcribe an audio file
docker run --gpus all -v $(pwd):/app whisper-transcriber /app/your_audio.mp3

# With custom model and output format
docker run --gpus all -v $(pwd):/app whisper-transcriber \
  /app/your_audio.mp3 --model large-v2 --output-format json --output-file transcript.json
```

### 3. Start API Server

```bash
# Start FastAPI server
docker run --gpus all -p 8000:8000 -v $(pwd):/app whisper-transcriber \
  /app/your_audio.mp3 --api --host 0.0.0.0 --port 8000
```

Then visit `http://localhost:8000/docs` for interactive API documentation.

## 📖 Detailed Usage

### Command Line Interface

```bash
python app.py <audio_file> [options]

Options:
  --model {tiny,base,small,medium,large,large-v2,large-v3}
                        Whisper model size (default: large-v3)
  --device {cuda,cpu}   Device to use (default: cuda)
  --compute-type {float16,float32,int8}
                        Compute type (default: float16)
  --output-format {text,json,srt}
                        Output format (default: text)
  --output-file FILE    Save output to file
  --api                 Start FastAPI server
  --host HOST           API host (default: 0.0.0.0)
  --port PORT           API port (default: 8000)
```

### Docker Examples

```bash
# Basic transcription
docker run --gpus all -v $(pwd):/app whisper-transcriber /app/audio.mp3

# Use smaller model for faster processing
docker run --gpus all -v $(pwd):/app whisper-transcriber \
  /app/audio.mp3 --model base

# Generate SRT subtitles
docker run --gpus all -v $(pwd):/app whisper-transcriber \
  /app/audio.mp3 --output-format srt --output-file subtitles.srt

# CPU-only mode (no GPU required)
docker run -v $(pwd):/app whisper-transcriber \
  /app/audio.mp3 --device cpu --model small
```

### API Usage

#### Upload and Transcribe

```bash
curl -X POST "http://localhost:8000/transcribe" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@audio.mp3" \
  -F "model_size=large-v3" \
  -F "output_format=json"
```

#### Response Format

```json
{
  "success": true,
  "result": {
    "file": "audio.mp3",
    "language": "en",
    "language_probability": 0.99,
    "duration": 120.5,
    "segments": [
      {
        "start": 0.0,
        "end": 3.2,
        "text": "Hello, this is a test transcription."
      }
    ]
  },
  "formatted_output": "..."
}
```

## ⚡ Performance Benchmarks

| Model Size | GPU Memory | Speed (RTF) | Quality |
|------------|------------|-------------|---------|
| tiny       | ~1GB       | 0.1x        | Good    |
| base       | ~1GB       | 0.2x        | Good    |
| small      | ~2GB       | 0.4x        | Very Good |
| medium     | ~5GB       | 0.6x        | Excellent |
| large      | ~10GB      | 1.0x        | Excellent |
| large-v2   | ~10GB      | 1.0x        | Excellent |
| large-v3   | ~10GB      | 1.0x        | Best     |

*RTF = Real Time Factor (1.0x = real-time, 0.1x = 10x faster than real-time)*

## 🏗️ Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Audio File    │───▶│  Docker Container │───▶│  Transcription  │
│  (MP3/WAV/etc)  │    │  + GPU Support    │    │   (Text/JSON)   │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                              │
                              ▼
                       ┌──────────────────┐
                       │  Faster-Whisper  │
                       │  + CUDA Runtime  │
                       └──────────────────┘
```

## 🔧 Configuration

### Environment Variables

```bash
# Optional: Set default model
export WHISPER_MODEL=large-v3

# Optional: Set default device
export WHISPER_DEVICE=cuda
```

### Docker Compose (Optional)

```yaml
version: '3.8'
services:
  whisper-transcriber:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - ./audio:/app/audio
    environment:
      - WHISPER_MODEL=large-v3
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: 1
              capabilities: [gpu]
```

## 📁 Project Structure

```
whisper-docker-transcriber/
├── Dockerfile              # GPU-enabled Docker configuration
├── requirements.txt        # Python dependencies
├── app.py                  # Main application (CLI + API)
├── README.md              # This file
├── .gitignore             # Git ignore rules
└── examples/              # Sample audio files
    └── sample_audio.mp3   # Example audio for testing
```

## 🛠️ Development

### Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run locally
python app.py audio.mp3

# Start API server
python app.py audio.mp3 --api
```

### Building Custom Images

```bash
# Build with specific CUDA version
docker build --build-arg CUDA_VERSION=11.8 -t whisper-transcriber:11.8 .

# Build for CPU-only
docker build --build-arg DEVICE=cpu -t whisper-transcriber:cpu .
```

## 🐛 Troubleshooting

### Common Issues

**GPU not detected:**
```bash
# Check NVIDIA Docker support
docker run --rm --gpus all nvidia/cuda:12.1.1-base-ubuntu22.04 nvidia-smi
```

**Out of memory:**
```bash
# Use smaller model
docker run --gpus all -v $(pwd):/app whisper-transcriber \
  /app/audio.mp3 --model small --compute-type int8
```

**Slow performance:**
```bash
# Ensure GPU is being used
docker run --gpus all -v $(pwd):/app whisper-transcriber \
  /app/audio.mp3 --device cuda --compute-type float16
```

## 📊 Supported Formats

### Input Audio Formats
- MP3, WAV, M4A, FLAC, OGG, AAC
- Any format supported by FFmpeg

### Output Formats
- **Text**: Human-readable transcript with timestamps
- **JSON**: Structured data with metadata
- **SRT**: SubRip subtitle format for video players

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [OpenAI Whisper](https://github.com/openai/whisper) - The original Whisper model
- [Faster-Whisper](https://github.com/SYSTRAN/faster-whisper) - Optimized Whisper implementation
- [NVIDIA CUDA](https://developer.nvidia.com/cuda-toolkit) - GPU acceleration support

## 📞 Support

- 🐛 **Issues**: [GitHub Issues](https://github.com/yourusername/whisper-docker-transcriber/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/yourusername/whisper-docker-transcriber/discussions)
- 📧 **Email**: your.email@example.com

---

**Made with ❤️ for the open-source community**