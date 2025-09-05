from enum import Enum

class PaymentStatus(str, Enum):
    PENDING = "pending"
    COMPLETED = "completed"
    FAILED = "failed"
    REFUNDED = "refunded"

class PaymentProvider(str, Enum):
    PAYSTACK = "paystack"
    SKRILL = "skrill"
    PAYPAL = "paypal"
    OPAY = "opay"
    BANK_TRANSFER = "bank_transfer"
    FLUTTERWAVE = "flutterwave"
