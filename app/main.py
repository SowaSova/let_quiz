from http import HTTPStatus

from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from starlette.responses import JSONResponse

from app.api.routers import main_router
from app.core.config import settings

app = FastAPI(title=settings.app_title)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=HTTPStatus.BAD_REQUEST,
        content={
            "detail": 'Запрос должен быть формата: {"questions_num": 10}'
        },
    )


app.include_router(main_router)
