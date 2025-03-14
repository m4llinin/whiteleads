import os
from dotenv import load_dotenv


load_dotenv(
    dotenv_path="env/prod.env",
)


class DBConfig:
    DB_USERNAME: str = os.getenv("DB_USERNAME")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD")
    DB_HOST: str = os.getenv("DB_HOST")
    DB_PORT: int = int(os.getenv("DB_PORT"))
    DB_DATABASE: str = os.getenv("DB_DATABASE")

    @property
    def URL(self) -> str:
        return (
            f"postgresql+asyncpg://{self.DB_USERNAME}:{self.DB_PASSWORD}"
            f"@{self.DB_HOST}:{self.DB_PORT}"
            f"/{self.DB_DATABASE}"
        )


class AuthConfig:
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORITHM: str = os.getenv("ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
    REFRESH_TOKEN_EXPIRE_DAYS: int = int(os.getenv("REFRESH_TOKEN_EXPIRE_DAYS"))


class ApiConfig:
    CORS_ORIGINS: list[str] = os.getenv("CORS_ORIGINS").split(",")
    CORS_CREDENTIALS: bool = bool(os.getenv("CORS_CREDENTIALS"))
    CORS_METHODS: list[str] = os.getenv("CORS_ORIGINS").split(",")
    CORS_HEADERS: list[str] = os.getenv("CORS_ORIGINS").split(",")


class Config:
    MODE: str = os.getenv("MODE")

    def __init__(self) -> None:
        self.db = DBConfig()
        self.auth = AuthConfig()
        self.api = ApiConfig()
