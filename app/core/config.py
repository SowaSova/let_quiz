from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_title: str = "Агрегатор вопросов для квизов"
    question_service: str = "https://jservice.io/api/"
    database_url: str = (
        "postgresql+asyncpg://postgres:postgres@db:5432/quiz_db"
    )
    postgres_db: str
    postgres_user: str
    postgres_password: str
    secret: str = "SECRET"

    class Config:
        env_file = ".env"


settings = Settings()
