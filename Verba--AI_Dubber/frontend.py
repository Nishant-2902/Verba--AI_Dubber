import streamlit as st
import requests

# Set up the page style
st.set_page_config(page_title="AI Video Dubber", page_icon="🎙️")
st.title("🎙️ AI Video Dubbing Studio")
st.write("Upload a video, choose a language, and let the AI pipeline do the rest!")

# Language dictionary mapping UI names to the codes our backend expects
LANGUAGE_MAP = {
    "Spanish (Spain)": "es",
    "French (France)": "fr",
    "Hindi (India)": "hi"
}

# UI Components
target_lang_name = st.selectbox("Select Target Language", list(LANGUAGE_MAP.keys()))
uploaded_file = st.file_uploader("Upload a Short Video", type=["mp4", "mkv", "avi", "mov"])

if st.button("Start Dubbing Pipeline"):
    if uploaded_file is not None:
        # Show a loading spinner while the backend does the heavy lifting
        with st.spinner(f"Dubbing into {target_lang_name}... This will take a moment on CPU."):
            
            # 1. Prepare the file and data to send to FastAPI
            url = "http://127.0.0.1:8000/dub-video"
            files = {"file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
            data = {"target_language": LANGUAGE_MAP[target_lang_name]}
            
            try:
                # 2. Send the request to your backend
                response = requests.post(url, files=files, data=data)
                
                # 3. Handle the returned video
                if response.status_code == 200:
                    st.success("Dubbing Complete! Watch your video below:")
                    
                    # Save the returned bytes to a temporary file to play it
                    output_video_path = "workspace/final_output.mp4"
                    with open(output_video_path, "wb") as f:
                        f.write(response.content)
                    
                    # Display the video player in the web UI
                    st.video(output_video_path)
                else:
                    st.error("Something went wrong with the backend processing.")
            except Exception as e:
                st.error(f"Could not connect to backend. Is the FastAPI server running? Error: {e}")
    else:
        st.warning("Please upload a video file first!")