import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "AI Cheat Sheet Builder"
    UPLOAD_DIR: str = "./data/uploads"
    PROCESSED_DIR: str = "./data/processed"

    # Add more configuration parameters as needed, such as database URL or API keys
    
    class Config:
        env_file = ".env"

settings = Settings()

# Ensure directories exist
os.makedirs(settings.UPLOAD_DIR, exist_ok=True)
os.makedirs(settings.PROCESSED_DIR, exist_ok=True)
