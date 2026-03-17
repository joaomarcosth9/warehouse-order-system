from fastapi import APIRouter, FastAPI

from app.api import router as api_router

app = FastAPI()

main_router = APIRouter()
main_router.include_router(api_router)

app.include_router(main_router)
