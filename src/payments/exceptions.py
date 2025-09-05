class PaymentException(Exception):
    def __init__(self, status_code: int = 500, detail: str = "An error occurred during payment processing."):
        self.status_code = status_code
        self.detail = detail
        super().__init__(self.detail)

class InvalidProviderException(PaymentException):
    def __init__(self, status_code: int = 400, detail: str = "The specified payment provider is not valid."):
        super().__init__(status_code, detail)
