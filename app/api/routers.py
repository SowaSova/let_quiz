from fastapi import APIRouter

from app.api.endpoints import quiz_router

main_router = APIRouter()
main_router.include_router(quiz_router)
