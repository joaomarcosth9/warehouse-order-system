from fastapi import APIRouter

from app.api.orders import router as orders_router

router = APIRouter()


@router.get("/")
def healthcheck():
    return {"status": "ok"}


router.include_router(orders_router)

__all__ = ["router"]
