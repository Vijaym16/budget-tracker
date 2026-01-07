from pydantic import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Budget Tracker API"
    DATABASE_URL: str = "sqlite:///./dev.db"   # simple for local dev
    SECRET_KEY: str = "change-this-key"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7

    class Config:
        env_file = ".env"

settings = Settings()