import streamlit as st
import tempfile
import os
from pathlib import Path
import sys

# Add the parent directory to the path to import our app
sys.path.append(str(Path(__file__).parent.parent))
from scripts.app import WhisperTranscriber

def main():
    st.set_page_config(
        page_title="Whisper Transcriber",
        page_icon="🎤",
        layout="wide"
    )
    
    st.title("🎤 Whisper Audio Transcriber")
    st.markdown("**Upload an audio file and get instant transcription!**")
    
    # Sidebar for settings
    with st.sidebar:
        st.header("⚙️ Settings")
        
        model_size = st.selectbox(
            "Model Size",
            ["tiny", "base", "small", "medium", "large", "large-v2", "large-v3"],
            index=6,  # Default to large-v3
            help="Larger models are more accurate but slower"
        )
        
        device = st.selectbox(
            "Device",
            ["cuda", "cpu"],
            index=0,
            help="CUDA requires GPU support"
        )
        
        output_format = st.selectbox(
            "Output Format",
            ["text", "json", "srt"],
            index=0,
            help="Choose output format"
        )
        
        compute_type = st.selectbox(
            "Compute Type",
            ["float16", "float32", "int8"],
            index=0,
            help="float16 is fastest, int8 uses least memory"
        )
    
    # Main content
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.header("📁 Upload Audio File")
        
        uploaded_file = st.file_uploader(
            "Choose an audio file",
            type=['mp3', 'wav', 'm4a', 'flac', 'ogg', 'aac'],
            help="Supported formats: MP3, WAV, M4A, FLAC, OGG, AAC"
        )
        
        if uploaded_file is not None:
            st.success(f"✅ File uploaded: {uploaded_file.name}")
            st.info(f"📊 File size: {uploaded_file.size / 1024 / 1024:.2f} MB")
    
    with col2:
        st.header("🚀 Transcribe")
        
        if uploaded_file is not None:
            if st.button("🎯 Start Transcription", type="primary"):
                with st.spinner("🔄 Transcribing audio... This may take a moment."):
                    try:
                        # Save uploaded file temporarily
                        with tempfile.NamedTemporaryFile(delete=False, suffix=f".{uploaded_file.name.split('.')[-1]}") as tmp_file:
                            tmp_file.write(uploaded_file.getvalue())
                            tmp_path = tmp_file.name
                        
                        # Initialize transcriber
                        transcriber = WhisperTranscriber(
                            model_size=model_size,
                            device=device,
                            compute_type=compute_type
                        )
                        
                        # Transcribe
                        result = transcriber.transcribe_file(tmp_path, output_format)
                        formatted_output = transcriber.format_output(result, output_format)
                        
                        # Clean up temp file
                        os.unlink(tmp_path)
                        
                        st.success("✅ Transcription completed!")
                        
                        # Display results
                        st.header("📝 Transcription Results")
                        
                        # Language info
                        col_lang, col_dur = st.columns(2)
                        with col_lang:
                            st.metric("Detected Language", result['language'])
                        with col_dur:
                            st.metric("Duration", f"{result['duration']:.1f}s")
                        
                        # Transcript
                        st.subheader("📄 Transcript")
                        st.text_area("Transcription", formatted_output, height=300)
                        
                        # Download button
                        st.download_button(
                            label=f"💾 Download as {output_format.upper()}",
                            data=formatted_output,
                            file_name=f"transcript.{output_format}",
                            mime="text/plain"
                        )
                        
                        # Segments table
                        if result['segments']:
                            st.subheader("⏱️ Segments")
                            segments_data = []
                            for i, segment in enumerate(result['segments'], 1):
                                segments_data.append({
                                    "Segment": i,
                                    "Start": f"{segment['start']:.2f}s",
                                    "End": f"{segment['end']:.2f}s",
                                    "Text": segment['text']
                                })
                            
                            st.dataframe(segments_data, use_container_width=True)
                        
                    except Exception as e:
                        st.error(f"❌ Error during transcription: {str(e)}")
                        st.info("💡 Try using a smaller model or CPU device if you're having issues.")
        else:
            st.info("👆 Please upload an audio file to get started!")
    
    # Footer
    st.markdown("---")
    st.markdown(
        "**Powered by OpenAI Whisper** | "
        "[GitHub](https://github.com/yourusername/whisper-docker-transcriber) | "
        "[Documentation](docs/README.md)"
    )

if __name__ == "__main__":
    main()
