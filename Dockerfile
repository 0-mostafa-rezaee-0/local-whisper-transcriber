# ==========================================
# Whisper Transcriber – GPU Dockerfile
# ==========================================
FROM nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04

WORKDIR /app

# 1️⃣ System deps
RUN apt-get update && apt-get install -y ffmpeg git python3 python3-pip && \
    rm -rf /var/lib/apt/lists/*

# 2️⃣ Install Python deps (use Faster-Whisper for speed)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 3️⃣ Copy app code
COPY scripts/ ./scripts/

# 4️⃣ Default command (can be overridden)
CMD ["python3", "scripts/app.py", "--help"]
