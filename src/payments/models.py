from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime
from src.payments.constants import PaymentStatus, PaymentProvider

class Payment(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: str = Field(index=True)
    amount: float
    currency: str
    status: PaymentStatus = Field(default=PaymentStatus.PENDING)
    provider: PaymentProvider
    transaction_id: str = Field(index=True, unique=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)