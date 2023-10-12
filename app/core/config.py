from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_title: str = "Вопросы для квиза"
    question_service: str = "https://jservice.io/api/"
    database_url: str = (
        "postgresql+asyncpg://postgres:postgres@db:5432/quiz_db"
    )
    postgres_db: str = "quiz_db"
    postgres_user: str = "postgres"
    postgres_password: str = "postgres"

    class Config:
        env_file = ".env"


settings = Settings()
