# AI Video Dubbing Studio

An end-to-end, fully automated AI video dubbing pipeline designed to transcribe, translate, and re-voice videos seamlessly. By combining highly optimized open-source AI models with fast, responsive network APIs, this application delivers an ultra-efficient media processing pipeline. The entire ecosystem is architected to prioritize streamlined asset rendering, low-latency execution, and minimal resource footprints while providing studio-quality voice translation and video synchronization.

---

## Key Features

- **Optimized Transcription Engine** — Utilizes advanced 8-bit quantization configurations to handle local speech-to-text processing with minimal hardware overhead.
- **Neural Voice Synthesis** — Leverages state-of-the-art cloud network architectures to generate natural-sounding, expressive human voices instantly.
- **Precision Timing & Alignment** — Translates scripts segment-by-segment while strictly preserving original timestamps to maintain perfect video pacing.
- **Production-Ready Containerization** — Fully containerized using Docker Compose for seamless, multi-service deployment with isolated environments.
- **Robust Automated Testing** — Ships with a robust test suite powered by pytest to ensure continuous integration safety and route stability.
- **Interactive Web Dashboard** — Features a clean, responsive Streamlit interface that lets users upload, process, and download dubbed media effortlessly.

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
| Testing Suite | Pytest / HTTPX | Testing frameworks utilized for automated endpoint verification. |
| Containerization | Docker / Compose | Container platform used to orchestrate application deployment layers. |

---

## Demo & Media

- 🎬 **YouTube Walkthrough:** [Watch the Video Demo Here](https://youtu.be/46Y4E4o1xaU)
- 💼 **LinkedIn Profile:** [Connect with me on LinkedIn](https://www.linkedin.com/in/nishant-sharma-29022004n/)

---

## Docker Deployment (Recommended)

The fastest way to deploy and run the entire stack with isolated networking is using Docker Compose. Ensure you have **Docker Desktop** installed and running on your machine.

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-video-dubber.git
cd ai-video-dubber
```

### 2. Launch the Container Stack

Run the following command from the root directory (where `docker-compose.yml` is located):

```bash
docker compose up --build
```

### 3. Access the Application

| Service | URL |
|---|---|
| Interactive Web UI | http://localhost:8501 |
| FastAPI Backend Docs | http://localhost:8000/docs |

---

##  Automated Testing

This project includes automated test configurations to validate API functionality, format handling, and localized configurations.

To execute the test suite within your active local virtual environment, navigate to the core module directory and run:

```bash
cd verba--AI_dubber
.\venv\Scripts\python.exe -m pytest -v
```

---

##  Manual Local Setup (Alternative)

If you prefer to run the application components outside of Docker, follow these local execution guidelines.

### 1. Environment Initialization

Navigate into the application folder and build an isolated virtual environment:

```bash
cd verba--AI_dubber
python -m venv venv

# Windows Activation
.\venv\Scripts\activate

# macOS/Linux Activation
source venv/bin/activate
```

### 2. Dependencies Setup

Install the optimized compute variant of PyTorch followed by the rest of the web packages:

```bash
.\venv\Scripts\python.exe -m pip install torch --index-url https://download.pytorch.org/whl/cpu
.\venv\Scripts\python.exe -m pip install -r requirements.txt
```

### 3. Execution

You will need to run the Backend Engine and the Web UI simultaneously in two separate terminal windows.

**Terminal 1 — Backend Server:**

```bash
.\venv\Scripts\python.exe -m uvicorn main:app --reload
```

**Terminal 2 — Frontend Dashboard:**

```bash
.\venv\Scripts\python.exe -m streamlit run frontend.py
```

---

##  Project Structure

```
ai-video-dubber/
│
├── verba--AI_dubber/
│   ├── Dockerfile.backend      # API backend container construction rules
│   ├── Dockerfile.frontend     # Web application container construction rules
│   ├── requirements.txt        # Python package version definitions
│   ├── main.py                 # Core FastAPI backend processing server
│   ├── frontend.py             # Streamlit application layout configuration
│   └── test_main.py            # Automated Pytest suite configuration
│
├── docker-compose.yml          # Container assembly engine orchestrator
└── README.md                   # Main technical documentation hub
```