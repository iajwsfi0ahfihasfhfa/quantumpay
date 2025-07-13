from fastapi import FastAPI
from app.routes import payments, auth

app = FastAPI(
    title="QuantumPay API",
    description="Modular payment gateway service",
    version="1.0.0"
)

app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
app.include_router(payments.router, prefix="/api/payments", tags=["payments"])

@app.get("/health")
def health_check():
    """
    Health check endpoint for monitoring.
    """
    return {"status": "ok"}
