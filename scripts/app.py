from faster_whisper import WhisperModel
import sys
import os
import argparse
from pathlib import Path
import json
from typing import Optional, List, Dict, Any

# Optional FastAPI imports
try:
    from fastapi import FastAPI, File, UploadFile, HTTPException
    from fastapi.responses import JSONResponse
    import uvicorn
    FASTAPI_AVAILABLE = True
except ImportError:
    FASTAPI_AVAILABLE = False

class WhisperTranscriber:
    def __init__(self, model_size: str = "large-v3", device: str = "cuda", compute_type: str = "float16"):
        """Initialize the Whisper transcriber with specified model and device settings."""
        self.model_size = model_size
        self.device = device
        self.compute_type = compute_type
        self.model = None
        
    def load_model(self):
        """Load the Whisper model (lazy loading for better performance)."""
        if self.model is None:
            print(f"Loading Whisper model: {self.model_size} on {self.device}")
            self.model = WhisperModel(
                self.model_size, 
                device=self.device, 
                compute_type=self.compute_type
            )
    
    def transcribe_file(self, audio_path: str, output_format: str = "text") -> Dict[str, Any]:
        """
        Transcribe an audio file and return results in specified format.
        
        Args:
            audio_path: Path to the audio file
            output_format: Output format ("text", "json", "srt")
            
        Returns:
            Dictionary containing transcription results
        """
        if not os.path.exists(audio_path):
            raise FileNotFoundError(f"Audio file not found: {audio_path}")
            
        self.load_model()
        
        print(f"Transcribing: {audio_path}")
        segments, info = self.model.transcribe(audio_path)
        
        # Convert segments to list for processing
        segments_list = list(segments)
        
        result = {
            "file": audio_path,
            "language": info.language,
            "language_probability": info.language_probability,
            "duration": info.duration,
            "segments": []
        }
        
        for segment in segments_list:
            segment_data = {
                "start": segment.start,
                "end": segment.end,
                "text": segment.text.strip()
            }
            result["segments"].append(segment_data)
        
        return result
    
    def format_output(self, result: Dict[str, Any], output_format: str) -> str:
        """Format the transcription result according to the specified output format."""
        if output_format == "json":
            return json.dumps(result, indent=2, ensure_ascii=False)
        
        elif output_format == "srt":
            srt_content = ""
            for i, segment in enumerate(result["segments"], 1):
                start_time = self._format_srt_time(segment["start"])
                end_time = self._format_srt_time(segment["end"])
                srt_content += f"{i}\n{start_time} --> {end_time}\n{segment['text']}\n\n"
            return srt_content
        
        else:  # text format
            text_content = f"Detected language: {result['language']} (confidence: {result['language_probability']:.2f})\n"
            text_content += f"Duration: {result['duration']:.2f} seconds\n\n"
            text_content += "--- Transcript ---\n\n"
            
            for segment in result["segments"]:
                text_content += f"[{segment['start']:.2f}s - {segment['end']:.2f}s]: {segment['text']}\n"
            
            return text_content
    
    def _format_srt_time(self, seconds: float) -> str:
        """Convert seconds to SRT time format (HH:MM:SS,mmm)."""
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        secs = int(seconds % 60)
        millisecs = int((seconds % 1) * 1000)
        return f"{hours:02d}:{minutes:02d}:{secs:02d},{millisecs:03d}"

def create_fastapi_app() -> FastAPI:
    """Create FastAPI application for web-based transcription."""
    if not FASTAPI_AVAILABLE:
        raise ImportError("FastAPI dependencies not installed. Run: pip install fastapi uvicorn python-multipart")
    
    app = FastAPI(
        title="Whisper Transcriber API",
        description="GPU-accelerated audio transcription using OpenAI Whisper",
        version="1.0.0"
    )
    
    transcriber = WhisperTranscriber()
    
    @app.get("/")
    async def root():
        return {"message": "Whisper Transcriber API", "status": "running"}
    
    @app.post("/transcribe")
    async def transcribe_audio(
        file: UploadFile = File(...),
        model_size: str = "large-v3",
        output_format: str = "json"
    ):
        """Transcribe uploaded audio file."""
        if not file.filename.lower().endswith(('.mp3', '.wav', '.m4a', '.flac', '.ogg')):
            raise HTTPException(status_code=400, detail="Unsupported file format")
        
        # Save uploaded file temporarily
        temp_path = f"/tmp/{file.filename}"
        with open(temp_path, "wb") as buffer:
            content = await file.read()
            buffer.write(content)
        
        try:
            # Update transcriber settings
            transcriber.model_size = model_size
            transcriber.model = None  # Force reload with new model
            
            # Transcribe
            result = transcriber.transcribe_file(temp_path, output_format)
            formatted_output = transcriber.format_output(result, output_format)
            
            return JSONResponse(content={
                "success": True,
                "result": result,
                "formatted_output": formatted_output
            })
            
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
        
        finally:
            # Clean up temporary file
            if os.path.exists(temp_path):
                os.remove(temp_path)
    
    return app

def main():
    """Main CLI function."""
    parser = argparse.ArgumentParser(description="GPU-accelerated audio transcription using OpenAI Whisper")
    parser.add_argument("audio_file", help="Path to the audio file to transcribe")
    parser.add_argument("--model", default="large-v3", 
                       choices=["tiny", "base", "small", "medium", "large", "large-v2", "large-v3"],
                       help="Whisper model size (default: large-v3)")
    parser.add_argument("--device", default="cuda", choices=["cuda", "cpu"],
                       help="Device to use for inference (default: cuda)")
    parser.add_argument("--compute-type", default="float16", 
                       choices=["float16", "float32", "int8"],
                       help="Compute type for inference (default: float16)")
    parser.add_argument("--output-format", default="text", 
                       choices=["text", "json", "srt"],
                       help="Output format (default: text)")
    parser.add_argument("--output-file", help="Save output to file instead of printing")
    parser.add_argument("--api", action="store_true", 
                       help="Start FastAPI server instead of CLI mode")
    parser.add_argument("--host", default="0.0.0.0", help="API host (default: 0.0.0.0)")
    parser.add_argument("--port", type=int, default=8000, help="API port (default: 8000)")
    
    args = parser.parse_args()
    
    if args.api:
        if not FASTAPI_AVAILABLE:
            print("Error: FastAPI dependencies not installed.")
            print("Install with: pip install fastapi uvicorn python-multipart")
            sys.exit(1)
        
        app = create_fastapi_app()
        print(f"Starting Whisper Transcriber API on http://{args.host}:{args.port}")
        uvicorn.run(app, host=args.host, port=args.port)
        return
    
    # CLI mode
    try:
        transcriber = WhisperTranscriber(
            model_size=args.model,
            device=args.device,
            compute_type=args.compute_type
        )
        
        result = transcriber.transcribe_file(args.audio_file, args.output_format)
        output = transcriber.format_output(result, args.output_format)
        
        if args.output_file:
            with open(args.output_file, 'w', encoding='utf-8') as f:
                f.write(output)
            print(f"Transcription saved to: {args.output_file}")
        else:
            print(output)
            
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
