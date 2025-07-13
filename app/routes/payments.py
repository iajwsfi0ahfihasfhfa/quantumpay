from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class PaymentRequest(BaseModel):
    amount: float
    currency: str
    method: str

@router.post("/")
def create_payment(request: PaymentRequest):
    # Simulated payment processing
    if request.amount <= 0:
        raise HTTPException(status_code=400, detail="Invalid amount")
    return {"payment_id": "pay_mock_123", "status": "processing"}

@router.get("/{payment_id}")
def get_payment(payment_id: str):
    # Simulated status retrieval
    if payment_id != "pay_mock_123":
        raise HTTPException(status_code=404, detail="Payment not found")
    return {"payment_id": payment_id, "status": "processing"}
