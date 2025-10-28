#!/bin/bash

# Whisper Docker Transcriber - One-Command Setup
# This script makes everything automatic - just run ./start.sh

set -e  # Exit on any error

echo "🎤 Whisper Docker Transcriber - Automated Setup"
echo "================================================"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    print_error "Docker is not installed. Please install Docker first."
    exit 1
fi

# Check if Docker is running
if ! docker info &> /dev/null; then
    print_error "Docker is not running. Please start Docker first."
    exit 1
fi

# Check for GPU support
if command -v nvidia-smi &> /dev/null; then
    print_success "NVIDIA GPU detected - GPU acceleration enabled"
    GPU_FLAG="--gpus all"
else
    print_warning "No NVIDIA GPU detected - using CPU mode"
    GPU_FLAG=""
fi

print_status "Building Docker image..."
docker build -t whisper-transcriber .

if [ $? -eq 0 ]; then
    print_success "Docker image built successfully!"
else
    print_error "Failed to build Docker image"
    exit 1
fi

# Ask user which interface they want
echo ""
echo "Choose your interface:"
echo "1) Web Interface (Easiest - Drag & Drop)"
echo "2) API Interface (For developers)"
echo "3) Command Line Interface"
echo ""
read -p "Enter your choice (1-3): " choice

case $choice in
    1)
        print_status "Starting Streamlit web interface..."
        print_status "Opening http://localhost:8501 in your browser..."
        
        # Try to open browser (works on most systems)
        if command -v xdg-open &> /dev/null; then
            xdg-open http://localhost:8501 &
        elif command -v open &> /dev/null; then
            open http://localhost:8501 &
        fi
        
        docker run $GPU_FLAG -p 8501:8501 -v "$(pwd):/app" whisper-transcriber \
            streamlit run scripts/web_app.py --server.port=8501 --server.address=0.0.0.0
        ;;
    2)
        print_status "Starting FastAPI interface..."
        print_status "Opening http://localhost:8000/docs in your browser..."
        
        # Try to open browser
        if command -v xdg-open &> /dev/null; then
            xdg-open http://localhost:8000/docs &
        elif command -v open &> /dev/null; then
            open http://localhost:8000/docs &
        fi
        
        docker run $GPU_FLAG -p 8000:8000 -v "$(pwd):/app" whisper-transcriber \
            python scripts/app.py /app/audio.mp3 --api --host 0.0.0.0 --port 8000
        ;;
    3)
        print_status "Starting command line interface..."
        echo ""
        echo "Usage examples:"
        echo "  docker run $GPU_FLAG -v \$(pwd):/app whisper-transcriber /app/your_audio.mp3"
        echo "  docker run $GPU_FLAG -v \$(pwd):/app whisper-transcriber /app/audio.mp3 --model large-v2"
        echo ""
        echo "Place your audio files in the current directory and run:"
        echo "  docker run $GPU_FLAG -v \$(pwd):/app whisper-transcriber /app/FILENAME"
        ;;
    *)
        print_error "Invalid choice. Please run the script again and choose 1, 2, or 3."
        exit 1
        ;;
esac

print_success "Setup complete! Happy transcribing! 🎉"
