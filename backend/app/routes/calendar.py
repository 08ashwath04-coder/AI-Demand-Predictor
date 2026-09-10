from fastapi import APIRouter

router = APIRouter(prefix="/calendar", tags=["calendar"])


@router.get("/")
def calendar_events() -> dict[str, list]:
    return {"events": []}
