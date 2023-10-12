from http import HTTPStatus

from fastapi import HTTPException
from pydantic import BaseModel, validator


class QuestionsNum(BaseModel):
    questions_num: int

    @validator("questions_num")
    def check_questions_num(cls, v):
        if v <= 0:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail="questions_num должно быть больше 0",
            )
        return v
