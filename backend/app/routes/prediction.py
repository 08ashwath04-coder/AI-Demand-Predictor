from fastapi import APIRouter

router = APIRouter(prefix="/predictions", tags=["predictions"])


@router.get("/")
def predictions() -> dict[str, list]:
    return {"items": []}
