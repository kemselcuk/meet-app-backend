from pydantic import BaseSettings
import os

class Settings(BaseSettings):
    # Database Configuration
    DATABASE_URL: str = "postgresql://user:password@localhost/meetingapp"
    
    # Security Settings
    SECRET_KEY: str = os.urandom(32).hex()  # Generates a random secret key
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # Application Settings
    PROJECT_NAME: str = "Meeting App Backend"
    DEBUG: bool = False
    
    # Cors Settings
    BACKEND_CORS_ORIGINS: list = [
        "http://localhost:3000",  # React Native development server
        "http://localhost:8081",  # Expo development server
    ]
    
    class Config:
        # Allows reading from .env file
        env_file = ".env"
        env_file_encoding = "utf-8"

# Create settings instance
settings = Settings()
