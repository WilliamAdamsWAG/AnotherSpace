import re

def validate_email(email: str) -> bool:
    """
    Validates an email address using a regular expression.

    Args:
        `email (str)`: Email address to be validated.

    Returns:
        `bool`: `True` if the email is valid, `False` otherwise.

    Example:
        >>> validate_email("example@example.com")
        True
        >>> validate_email("invalid_email")
        False
    """
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    if re.fullmatch(regex, email):
        return True
    else:
        return False