import secrets
import string

def generate_reference(length: int = 12) -> str:
    """
    Generates a unique payment reference.
    """
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for i in range(length))