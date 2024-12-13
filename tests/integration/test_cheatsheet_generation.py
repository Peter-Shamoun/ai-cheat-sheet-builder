from fastapi.testclient import TestClient
from main import app
import os

client = TestClient(app)

def test_generate_cheat_sheet():
    """
    Test the /generate endpoint to ensure it processes a document
    and returns the path to the generated cheat sheet.
    """
    # Create a temporary test file
    temp_file_path = "test_document.txt"
    with open(temp_file_path, "w") as f:
        f.write("This is a test document.\n\nKey content for the cheat sheet.")

    with open(temp_file_path, "rb") as file:
        response = client.post("/generate", files={"file": file})

    # Assertions
    assert response.status_code == 200
    assert "pdf_path" in response.json()

    # Cleanup
    os.remove(temp_file_path)
    generated_file_path = response.json()["pdf_path"]
    if os.path.exists(generated_file_path):
        os.remove(generated_file_path)
