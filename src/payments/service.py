import uuid
from sqlmodel import Session
from src.payments.models import Payment
from src.payments.schema import PaymentCreate, WebhookPayload
from src.payments.constants import PaymentStatus, PaymentProvider
from src.payments.exceptions import PaymentException, InvalidProviderException
from typing import Dict, Any

# Mock external payment provider clients
class PaymentGateway:
    def __init__(self, provider: PaymentProvider):
        self.provider = provider

    def create_charge(self, amount: float, currency: str) -> Dict[str, Any]:
        print(f"Creating charge with {self.provider.value} for {amount} {currency}")
        return {"id": f"mock_{uuid.uuid4()}", "status": "succeeded"}

    def verify_webhook(self, payload: WebhookPayload) -> bool:
        # In a real app, you'd verify the signature here
        print(f"Verifying webhook from {self.provider.value}")
        return True

def get_payment_gateway(provider: PaymentProvider) -> PaymentGateway:
    if provider not in PaymentProvider:
        raise InvalidProviderException(detail=f"Provider '{provider}' is not supported.")
    return PaymentGateway(provider)


def create_payment(db: Session, payment: PaymentCreate) -> Payment:
    """
    Creates a new payment record and initiates payment with the provider.
    """
    transaction_id = f"txn_{uuid.uuid4().hex}"

    try:
        gateway = get_payment_gateway(payment.provider)
        charge = gateway.create_charge(payment.amount, payment.currency)

        db_payment = Payment(
            user_id=payment.user_id,
            amount=payment.amount,
            currency=payment.currency,
            provider=payment.provider,
            status=PaymentStatus.COMPLETED if charge.get('status') == 'succeeded' else PaymentStatus.FAILED,
            transaction_id=transaction_id,
        )
        db.add(db_payment)
        db.commit()
        db.refresh(db_payment)
        return db_payment
    except Exception as e:
        db.rollback()
        raise PaymentException(detail=f"Failed to create payment: {str(e)}")


def get_payment_by_transaction_id(db: Session, transaction_id: str):
    """
    Retrieves a payment by its transaction ID.
    """
    return db.query(Payment).filter(Payment.transaction_id == transaction_id).first()


async def process_webhook(db: Session, provider: str, payload: WebhookPayload):
    """
    Processes incoming webhooks from payment providers.
    """
    try:
        provider_enum = PaymentProvider(provider.lower())
        gateway = get_payment_gateway(provider_enum)
    except (ValueError, InvalidProviderException) as e:
        raise InvalidProviderException(detail=str(e))

    if not gateway.verify_webhook(payload):
        raise PaymentException(status_code=400, detail="Webhook verification failed.")

    # Process based on event type
    event_type = payload.event
    data = payload.data
    transaction_id = data.get("transaction_id")

    if not transaction_id:
        raise PaymentException(status_code=400, detail="Missing transaction_id in webhook payload.")

    db_payment = get_payment_by_transaction_id(db, transaction_id)
    if not db_payment:
        raise PaymentException(status_code=404, detail="Payment not found for webhook.")

    if event_type == "payment.succeeded":
        db_payment.status = PaymentStatus.COMPLETED
    elif event_type == "payment.failed":
        db_payment.status = PaymentStatus.FAILED
    else:
        print(f"Unhandled webhook event: {event_type}")
        return {"status": "unhandled event"}

    db.add(db_payment)
    db.commit()

    return {"status": "webhook processed successfully"}
