from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class LoginRequest(BaseModel):
    username: str
    password: str

@router.post("/login")
def login(request: LoginRequest):
    # Placeholder logic for authentication
    if request.username == "admin" and request.password == "admin":
        return {"token": "dummy-jwt-token"}
    raise HTTPException(status_code=401, detail="Invalid credentials")
