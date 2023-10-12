from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import QuizQuestion


async def question_exists(
    model: QuizQuestion, question_id: int, session: AsyncSession
) -> bool:
    """Проверка наличия вопроса в бд"""
    query = select(model).where(model.question_id == question_id)
    result = await session.execute(query)
    return result.scalar_one_or_none() is not None
