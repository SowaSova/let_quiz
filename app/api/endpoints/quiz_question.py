from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.crud import quiz_question_crud
from app.schemas.question_nums import QuestionsNum
from app.schemas.quiz_question import QuizQuestionDB

router = APIRouter()


@router.post(
    "/", response_model=list[QuizQuestionDB], response_model_exclude_none=True
)
async def get_questions(
    questions_num: QuestionsNum,
    session: AsyncSession = Depends(get_async_session),
):
    """Получаем вопросы для квиза"""
    data = await quiz_question_crud.get_questions_for_quiz(
        questions_num.questions_num, session
    )
    return data
