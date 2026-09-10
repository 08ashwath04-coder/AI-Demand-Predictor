from fastapi import APIRouter

router = APIRouter(prefix="/retailer", tags=["retailer"])


@router.get("/summary")
def retailer_summary() -> dict[str, str]:
    return {"status": "ready"}
