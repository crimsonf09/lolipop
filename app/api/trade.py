from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/trade")

class MarketData(BaseModel):
    price: float
    rsi: float

@router.post("/predict")
def predict(data: MarketData):
    if data.rsi < 30:
        return {"action": "BUY"}
    elif data.rsi > 70:
        return {"action": "SELL"}
    return {"action": "HOLD"}
