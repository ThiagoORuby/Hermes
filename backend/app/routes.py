from fastapi import APIRouter

router = APIRouter(prefix="/api", tags=["api"])


@router.get("")
def index():
    return "It's working!"
