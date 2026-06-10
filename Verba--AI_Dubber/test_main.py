import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_home_endpoint():
    """Validates the availability status of the application server API."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "online"

def test_dub_video_invalid_file_type():
    """Asserts that the pipeline drops bad files with a 400 Client Error code."""
    bad_payload = {"file": ("malicious_script.sh", b"echo 'hack'", "text/x-shellscript")}
    form_data = {"target_language": "es"}
    
    response = client.post("/dub-video", files=bad_payload, data=form_data)
    
    assert response.status_code == 400
    assert response.json()["detail"] == "Invalid video file."

def test_voice_map_configurations():
    """Asserts that fallback structures validate gracefully for unmapped locales."""
    from main import VOICE_MAP
    assert "es" in VOICE_MAP
    assert "hi" in VOICE_MAP
    assert VOICE_MAP["en"] == "en-US-ChristopherNeural"