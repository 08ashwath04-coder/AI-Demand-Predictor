from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import Base, engine
from app import models
from app.routers import auth as auth_router, calendar as calendar_router, demand, farmer, inventory, products, retailer

app = FastAPI(title="AI Demand Predictor API", version="0.1.0")

Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router.router)
app.include_router(calendar_router.router)
app.include_router(demand.router)
app.include_router(farmer.router)
app.include_router(inventory.router)
app.include_router(products.router)
app.include_router(retailer.router)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
