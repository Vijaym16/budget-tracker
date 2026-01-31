from pydantic import BaseSettings
from passlib.context import CryptContext
from datetime import timedelta

class Settings(BaseSettings):
    PROJECT_NAME: str = "Budget Tracker API"
    DATABASE_URL: str = "sqlite:///./dev.db"   # simple for local dev
    SECRET_KEY: str = "change-this-key"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7

    class Config:
        env_file = ".env"

settings = Settings()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

SECRET_KEY = "super-secret-key-change-later"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
