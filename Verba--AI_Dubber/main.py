import os
import asyncio
from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
# Import AudioFileClip for the final stitching
from moviepy import VideoFileClip, AudioFileClip
from faster_whisper import WhisperModel
from deep_translator import GoogleTranslator
import edge_tts

app = FastAPI(title="Optimized AI Video Dubbing API", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

WORKSPACE_DIR = "workspace"
os.makedirs(WORKSPACE_DIR, exist_ok=True)

print("--> Loading Whisper Model into RAM...")
whisper_model = WhisperModel("tiny", device="cpu", compute_type="int8")
print("--> Whisper Model loaded successfully!")

VOICE_MAP = {
    "es": "es-ES-AlvaroNeural", # Spanish
    "fr": "fr-FR-HenriNeural",  # French
    "hi": "hi-IN-MadhurNeural", # Hindi
    "en": "en-US-ChristopherNeural" # Default
}

@app.get("/")
def home():
    return {"status": "online", "message": "Dubbing Pipeline is live."}

@app.post("/dub-video")
async def dub_video(
    file: UploadFile = File(...),
    target_language: str = Form("es") 
):
    if not file.filename.lower().endswith(('.mp4', '.mkv', '.avi', '.mov')):
        raise HTTPException(status_code=400, detail="Invalid video file.")
    
    # 1. Save File
    video_path = os.path.join(WORKSPACE_DIR, f"input_{file.filename}")
    with open(video_path, "wb") as buffer:
        buffer.write(await file.read())
        
    # 2. Extract Audio
    audio_path = os.path.join(WORKSPACE_DIR, "extracted_audio.wav")
    print(f"--> Extracting audio from {file.filename}...")
    try:
        video_clip = VideoFileClip(video_path)
        video_clip.audio.write_audiofile(audio_path, logger=None)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Audio extraction failed: {str(e)}")

    # 3. Transcribe & 4. Translate
    print("--> Transcribing and Translating...")
    try:
        translator = GoogleTranslator(source='auto', target=target_language)
        segments, info = whisper_model.transcribe(audio_path, beam_size=5)
        
        full_translated_text = ""
        for segment in segments:
            full_translated_text += translator.translate(segment.text.strip()) + " "
            
        full_translated_text = full_translated_text.strip()

        # 5. Text-to-Speech (Generate Dubbed Audio)
        print(f"--> Generating new AI audio in '{target_language}'...")
        dubbed_audio_path = os.path.join(WORKSPACE_DIR, "dubbed_audio.mp3")
        voice = VOICE_MAP.get(target_language, VOICE_MAP["en"])
        
        communicate = edge_tts.Communicate(full_translated_text, voice)
        await communicate.save(dubbed_audio_path)
        
        # 6. Stitching: Attach new audio to original video
        print("--> Stitching new audio onto the video... (This might take a few seconds)")
        final_video_path = os.path.join(WORKSPACE_DIR, f"final_dubbed_{file.filename}")
        
        # Load the new audio
        new_audio = AudioFileClip(dubbed_audio_path)
        
        # In MoviePy v2.0, we use with_audio() to set the audio track
        final_video = video_clip.with_audio(new_audio)
        
        # Render the final file
        final_video.write_videofile(
            final_video_path, 
            codec="libx264", 
            audio_codec="aac", 
            logger=None
        )
        
        # Cleanup memory
        video_clip.close()
        new_audio.close()
        final_video.close()
        
        print("--> Pipeline Complete!")
        
        # Return the actual video file to the user!
        return FileResponse(
            path=final_video_path, 
            media_type="video/mp4", 
            filename=f"dubbed_{target_language}_{file.filename}"
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Processing failed: {str(e)}")