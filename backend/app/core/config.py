from typing import List
import os

try:
    from pydantic_settings import BaseSettings, SettingsConfigDict
except ImportError:
    from pydantic import BaseModel

    class BaseSettings(BaseModel):  # type: ignore
        def __init__(self, **values):
            # Populate from environment variables if present
            super().__init__(**values)
            for field in self.model_fields:
                env_val = os.getenv(field)
                if env_val is not None:
                    setattr(self, field, env_val)

    SettingsConfigDict = dict  # type: ignore


class Settings(BaseSettings):
    PROJECT_NAME: str = "AI Site Engineer"
    VERSION: str = "0.1.0"
    ENVIRONMENT: str = "development"
    DEBUG: bool = True
    API_V1_STR: str = "/api/v1"

    # CORS
    BACKEND_CORS_ORIGINS: List[str] = [
        "http://localhost:3000",
        "http://localhost:8000",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:8000",
    ]

    # Database
    DATABASE_URL: str = "sqlite:///./ai_site_engineer.db"
    POSTGRES_SERVER: str = "localhost"
    POSTGRES_PORT: int = 5432
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "password"
    POSTGRES_DB: str = "ai_site_engineer"

    # LLM Settings
    LLM_PROVIDER: str = "openai"
    OPENAI_API_KEY: str = ""
    EMBEDDING_MODEL: str = "text-embedding-3-small"
    ORCHESTRATOR_MODEL: str = "gpt-4o"

    # Storage
    UPLOAD_DIR: str = "./uploads"
    MAX_UPLOAD_SIZE_MB: int = 50

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore",
    )


settings = Settings()
