from datetime import datetime as dt
from typing import Optional

import aiohttp
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import settings
from app.crud.base import CRUDBase
from app.models.quiz_question import QuizQuestion
from app.services.validators import question_exists


class CRUDQuizQuestion(CRUDBase):
    async def get_questions_for_quiz(self, amount: int, session: AsyncSession):
        """Получаем вопросы для квиза"""
        check_counter = 0  # Счетчик проверок
        max_checks = 10000  # Лимит количества проверок
        sent_question_ids = []  # Список отправленных вопросов
        async with aiohttp.ClientSession() as http_session:
            link = f"{settings.question_service}/random?count={amount}"
            async with http_session.get(link) as resp:
                data = await resp.json()
                for question in data:
                    filtered_data = {
                        key: question[key] for key in ("question", "answer")
                    }
                    filtered_data["question_id"] = question["id"]
                    # Проверяем на наличие в вопроса в бд
                    exists = await question_exists(
                        self.model, filtered_data["question_id"], session
                    )
                    # Добавляем вопрос в бд, если его нет
                    if not exists:
                        date_obj = dt.strptime(
                            question["created_at"], "%Y-%m-%dT%H:%M:%S.%fZ"
                        )
                        filtered_data["created_at"] = date_obj
                        db_obj = self.model(**filtered_data)
                        session.add(db_obj)
                        await session.commit()
                        await session.refresh(db_obj)
                    # Если вопрос уже есть в бд, то пропускаем его, ищем следующий
                    check_counter += 1
                    # Если количество проверок превысило лимит, то возвращаем случайный вопрос из бд
                    if check_counter >= max_checks:
                        random_question = await self.get_random_question(
                            session, sent_question_ids
                        )
                        # Добавляем вопрос в список отправленных вопросов, чтобы не повторять его
                        sent_question_ids.append(random_question.question_id)
                        return random_question

                return data

    async def get_random_question(
        self, session: AsyncSession, sent_questions: list
    ) -> QuizQuestion:
        """Получение случайного вопроса из бд"""
        limiter = 1
        query = (
            select(self.model)
            .where(self.model.question_id.notin_(sent_questions))
            .order_by(func.random())
            .limit(limiter)
        )
        result = await session.execute(query)
        return result.scalar_one()


quiz_question_crud = CRUDQuizQuestion(QuizQuestion)
