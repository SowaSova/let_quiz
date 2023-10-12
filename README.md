# Поиск вопросов для квиза

### Установка приложения через Docker

Склонировать проект
```
git clone git@github.com:SowaSova/let_quiz.git & cd let_quiz/
```

Переименовать файл .env_example в .env или создать новый с содержимым:
```
POSTGRES_PASSWORD=postgres
POSTGRES_USER=postgres
POSTGRES_DB=quiz_db
APP_TITLE=Вопросы для квиза
DATABASE_URL=postgresql+asyncpg://postgres:postgres@db:5432/quiz_db
```

Запустить контейнер
```
docker-compose up -d --build
```

После запуска документация будет по [ссылке](http://127.0.0.1:8000/docs)

