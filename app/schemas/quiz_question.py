from datetime import datetime

from pydantic import BaseModel


class QuizQuestionBase(BaseModel):
    question: str
    answer: str
    created_at: datetime


class QuizQuestionDB(QuizQuestionBase):
    pass


class QuizQuestionCreate(QuizQuestionBase):
    id: int

    class Config:
        from_attributes = True
