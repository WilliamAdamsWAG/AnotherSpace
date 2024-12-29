import pytest

from src.AnotherSpace.Validator import validate_email

@pytest.mark.parametrize(
    ("email", "result"),
    [
        ("example@example.com", True),
        ("Example@examplecom", False),
        ("Example@example.", False),
        ("!Example@example.com", False),
        ("exampleexample.com", False),
        ("@example.com", False)
    ]
)
def test_email_validate(email: str, result: bool):
    assert validate_email(email) == result
