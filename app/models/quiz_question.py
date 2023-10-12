from sqlalchemy import Column, DateTime, Integer, Text

from .base import AbstractBase


class QuizQuestion(AbstractBase):
    question_id = Column(Integer)
    question = Column(Text, nullable=False)
    answer = Column(Text, nullable=False)
    created_at = Column(DateTime)
