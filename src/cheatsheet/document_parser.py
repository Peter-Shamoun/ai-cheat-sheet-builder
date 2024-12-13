from PyPDF2 import PdfReader
from docx import Document

def extract_text_from_file(file_path: str) -> str:
    """
    Extracts text from a file based on its type.

    Args:
        file_path (str): Path to the file.

    Returns:
        str: Extracted text from the file.
    """
    if file_path.endswith('.pdf'):
        reader = PdfReader(file_path)
        return " ".join([page.extract_text() for page in reader.pages])

    elif file_path.endswith('.docx'):
        doc = Document(file_path)
        return "\n".join([para.text for para in doc.paragraphs])

    else:
        with open(file_path, 'r') as file:
            return file.read()
