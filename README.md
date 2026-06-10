# AI Video Dubbing Studio

An end-to-end, fully automated AI video dubbing pipeline that transcribes, translates, and re-voices videos seamlessly. By combining highly optimized open-source AI models with fast, responsive network APIs, this application delivers an efficient media processing pipeline with studio-quality voice translation and video synchronization.

---

## Key Features

- **Efficient Local Transcription** — Utilizes high-performance 8-bit quantization to run speech-to-text locally with a remarkably lightweight resource footprint.
- **Neural Voice Generation** — Leverages state-of-the-art cloud network architectures to synthesize natural-sounding, expressive human voices instantly.
- **Smart Timestamp Mapping** — Translates text line-by-line while strictly preserving original video timing constraints for accurate pacing.
- **Asynchronous API Architecture** — Built on a robust backend capable of handling video file streams and concurrent processing tasks smoothly.
- **Interactive Web Dashboard** — Features a clean, responsive web interface that allows users to upload, process, and preview dubbed media without using a command line.

---

## Technology Stack

| Component | Technology | Description |
|---|---|---|
| Core Pipeline Server | FastAPI | Asynchronous, high-performance Python web API framework. |
| Frontend Web UI | Streamlit | Modern data-centric framework used to build the interactive studio interface. |
| Speech-to-Text | Faster-Whisper | A highly optimized, fast reimplementation of OpenAI's Whisper model. |
| Translation Engine | Deep-Translator | Flexible translation pipeline utilizing automated language detection. |
| Text-to-Speech (TTS) | Edge-TTS | Microsoft Edge's advanced neural network communication voices. |
| Video & Audio Editing | MoviePy v2.0 | Digital media processor used for track splitting and final audio-video stitching. |

---

## Demo & Media

- 🎬 **YouTube Walkthrough:** [Watch the Video Demo Here](https://youtu.be/46Y4E4o1xaU)
- 💼 **LinkedIn Profile:** [Connect with me on LinkedIn](https://www.linkedin.com/in/nishant-sharma-29022004n/)

---

##  Setup & Installation

### 1. Project Environment Setup

Open your terminal inside the project directory and create an isolated virtual environment to manage dependencies:

```bash
# Navigate to the core application directory
cd verba--AI_dubber

# Create virtual environment
python -m venv venv

# Activate the virtual environment (Windows)
.\venv\Scripts\activate

# Activate the virtual environment (macOS/Linux)
source venv/bin/activate
```

### 2. Installing Dependencies

Install the optimized version of PyTorch along with the necessary web and machine learning packages:

```bash
# Install PyTorch core configuration
.\venv\Scripts\python.exe -m pip install torch --index-url https://download.pytorch.org/whl/cpu

# Install the rest of the application packages
.\venv\Scripts\python.exe -m pip install fastapi uvicorn python-multipart moviepy faster-whisper deep-translator edge-tts streamlit requests
```

---

## Running the Application

This app uses a decoupled client-server architecture. You must launch the **Core Server** and the **Web UI** simultaneously in two separate terminal windows.

### Step 1 — Start the FastAPI Server

In your first terminal, ensure your environment is activated and start the backend pipeline:

```bash
.\venv\Scripts\python.exe -m uvicorn main:app --reload
```

> Wait until you see `Whisper Model loaded successfully!` in the logs before proceeding.

### Step 2 — Start the Streamlit Frontend

Open a second terminal window, ensure the virtual environment is active, and launch the dashboard:

```bash
.\venv\Scripts\python.exe -m streamlit run frontend.py
```

The interface will automatically open in your browser at **http://localhost:8501**.

---

## Project Structure

```
ai-video-dubber/
│
├── verba--AI_dubber/
│   ├── venv/              # Local isolated Python environment binaries
│   ├── workspace/         # Auto-generated directory for temporary rendering processes
│   ├── main.py            # Core FastAPI processing server
│   └── frontend.py        # Streamlit application rendering the web studio layout
│
└── README.md              # Project documentation hub
```