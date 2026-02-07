from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    LLM_URL: str
    DATABASE_URL: str = "sqlite:///db/chat.db"
    TIMEOUT: int = 30

    class Config:
        env_file = ".env"

settings = Settings()
