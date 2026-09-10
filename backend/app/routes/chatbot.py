from fastapi import APIRouter

router = APIRouter(prefix="/chatbot", tags=["chatbot"])


@router.get("/status")
def chatbot_status() -> dict[str, str]:
    return {"status": "ready"}
