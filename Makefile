# Whisper Docker Transcriber - Makefile
# Simple commands to make everything automatic

.PHONY: help build start-web start-api start-cli stop clean logs

# Default target
help:
	@echo "🎤 Whisper Docker Transcriber - Available Commands:"
	@echo ""
	@echo "  make build      - Build Docker image"
	@echo "  make start-web  - Start Streamlit web interface"
	@echo "  make start-api  - Start FastAPI interface"
	@echo "  make start-cli   - Show CLI usage examples"
	@echo "  make stop       - Stop all containers"
	@echo "  make clean      - Clean up containers and images"
	@echo "  make logs       - Show container logs"
	@echo ""
	@echo "Quick Start: make start-web"

# Build the Docker image
build:
	@echo "🔨 Building Docker image..."
	docker build -t whisper-transcriber .
	@echo "✅ Build complete!"

# Start Streamlit web interface
start-web:
	@echo "🌐 Starting Streamlit web interface..."
	@echo "📱 Open http://localhost:8501 in your browser"
	docker-compose up whisper-transcriber &
	@sleep 3
	@echo "🚀 Starting Streamlit..."
	docker-compose exec whisper-transcriber streamlit run scripts/web_app.py --server.port=8501 --server.address=0.0.0.0

# Start FastAPI interface
start-api:
	@echo "🔌 Starting FastAPI interface..."
	@echo "📱 Open http://localhost:8000/docs in your browser"
	docker-compose up whisper-transcriber &
	@sleep 3
	@echo "🚀 Starting FastAPI..."
	docker-compose exec whisper-transcriber python scripts/app.py /app/audio.mp3 --api --host 0.0.0.0 --port 8000

# Show CLI usage
start-cli:
	@echo "💻 Command Line Interface Usage:"
	@echo ""
	@echo "1. Place your audio file in this directory"
	@echo "2. Run: docker-compose exec whisper-transcriber python scripts/app.py /app/YOUR_FILE.mp3"
	@echo ""
	@echo "Examples:"
	@echo "  docker-compose exec whisper-transcriber python scripts/app.py /app/audio.mp3"
	@echo "  docker-compose exec whisper-transcriber python scripts/app.py /app/audio.mp3 --model large-v2"
	@echo "  docker-compose exec whisper-transcriber python scripts/app.py /app/audio.mp3 --output-format srt"

# Stop all containers
stop:
	@echo "🛑 Stopping containers..."
	docker-compose down
	@echo "✅ Stopped!"

# Clean up
clean:
	@echo "🧹 Cleaning up..."
	docker-compose down --volumes --remove-orphans
	docker rmi whisper-transcriber 2>/dev/null || true
	@echo "✅ Cleanup complete!"

# Show logs
logs:
	docker-compose logs -f whisper-transcriber
