import os
import pytest
from cheatsheet.document_parser import process_document

def test_process_document():
    """
    Test that the process_document function correctly processes a sample text file
    and returns the expected sections.
    """
    temp_file_path = "test_document.txt"
    
    # Create a temporary test file
    with open(temp_file_path, "w") as f:
        f.write("This is a test document.\n\nSection 1 content.\n\nSection 2 content.")

    # Process the file
    sections = process_document(temp_file_path)

    # Assertions
    assert len(sections) == 3
    assert sections[0] == "This is a test document."
    assert sections[1] == "Section 1 content."
    assert sections[2] == "Section 2 content."

    # Cleanup
    os.remove(temp_file_path)
