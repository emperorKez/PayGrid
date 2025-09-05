from pydantic import BaseModel, Field
from typing import Optional
from src.payments.constants import PaymentProvider

class PaymentCreate(BaseModel):
    user_id: str
    amount: float
    currency: str = "USD"
    provider: PaymentProvider

class PaymentResponse(BaseModel):
    id: int
    user_id: str
    amount: float
    currency: str
    status: str
    provider: str
    transaction_id: str

class PaymentUpdate(BaseModel):
    status: str

class WebhookPayload(BaseModel):
    event: str
    data: dict
