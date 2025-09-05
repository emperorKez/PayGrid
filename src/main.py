from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from src.payments.router import router as payment_router
from src.payments.exceptions import PaymentException

app = FastAPI(
    title="Payment Microservice",
    description="Handles payment generation, acceptance, and processing.",
    version="1.0.0"
)

# Exception handler for custom payment exceptions
@app.exception_handler(PaymentException)
async def payment_exception_handler(request: Request, exc: PaymentException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail},
    )

# Include the payment router
app.include_router(payment_router, prefix="/api/v1/payments", tags=["payments"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Payment Microservice"}