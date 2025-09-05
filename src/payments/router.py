from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from src.payments import service
from src.payments.schema import PaymentCreate, PaymentResponse, WebhookPayload
from src.core.database import get_db_session

router = APIRouter()

@router.post("/", response_model=PaymentResponse)
def create_payment(payment: PaymentCreate, db: Session = Depends(get_db_session)):
    """
    Create a new payment intent.
    """
    return service.create_payment(db=db, payment=payment)

@router.get("/{transaction_id}", response_model=PaymentResponse)
def get_payment(transaction_id: str, db: Session = Depends(get_db_session)):
    """
    Retrieve the status of a payment.
    """
    db_payment = service.get_payment_by_transaction_id(db, transaction_id)
    if db_payment is None:
        raise HTTPException(status_code=404, detail="Payment not found")
    return db_payment

@router.post("/webhook/{provider}")
async def handle_webhook(provider: str, payload: WebhookPayload, db: Session = Depends(get_db_session)):
    """
    Handle webhooks from payment providers.
    """
    return await service.process_webhook(db=db, provider=provider, payload=payload)
