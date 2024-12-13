from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import os
from cheatsheet.document_parser import process_document
from cheatsheet.cheatsheet_generator import CheatSheetGenerator

# Initialize FastAPI application
app = FastAPI(title="AI Cheat Sheet Builder", version="1.0.0")

# CORS Middleware setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health check endpoint
@app.get("/health")
async def health_check():
    return JSONResponse(content={"status": "OK"}, status_code=200)

# File upload endpoint
@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    try:
        upload_dir = "./data/uploads"
        os.makedirs(upload_dir, exist_ok=True)

        file_path = os.path.join(upload_dir, file.filename)
        with open(file_path, "wb") as f:
            content = await file.read()
            f.write(content)

        return {"message": "File uploaded successfully.", "file_path": file_path}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Cheat sheet generation endpoint
@app.post("/generate")
async def generate_cheat_sheet(file: UploadFile = File(...)):
    try:
        upload_dir = "./data/uploads"
        output_dir = "./data/processed"
        template_dir = "./cheatsheet/templates"

        os.makedirs(upload_dir, exist_ok=True)
        os.makedirs(output_dir, exist_ok=True)

        # Save the uploaded file
        file_path = os.path.join(upload_dir, file.filename)
        with open(file_path, "wb") as f:
            content = await file.read()
            f.write(content)

        # Process the document
        sections = process_document(file_path)

        # Generate the cheat sheet
        generator = CheatSheetGenerator(template_dir=template_dir, output_dir=output_dir)
        output_name = os.path.splitext(file.filename)[0]
        pdf_path = generator.generate_cheat_sheet(sections=sections, output_name=output_name)

        return {"message": "Cheat sheet generated successfully.", "pdf_path": pdf_path}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
