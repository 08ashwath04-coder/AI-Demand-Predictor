from fastapi import APIRouter

router = APIRouter(prefix="/farmer", tags=["farmer"])


@router.get("/summary")
def farmer_summary() -> dict[str, str]:
    return {"status": "ready"}
