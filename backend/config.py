import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")
    SECRET_KEY = os.getenv("SECRET_KEY", "super-secret")
    EMAIL_HOST = os.getenv("EMAIL_HOST", "smtp.gmail.com")
    EMAIL_PORT = int(os.getenv("EMAIL_PORT", 587))
    EMAIL_USERNAME = os.getenv("EMAIL_USERNAME", "")
    EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD", "")
    TWILIO_SID = os.getenv("TWILIO_SID", "")
    TWILIO_TOKEN = os.getenv("TWILIO_TOKEN", "")
    TWILIO_PHONE = os.getenv("TWILIO_PHONE", "")
    GITHUB_CLIENT_ID = os.getenv("GITHUB_CLIENT_ID", "")
    GITHUB_CLIENT_SECRET = os.getenv("GITHUB_CLIENT_SECRET", "")

settings = Settings()
