import pytest

from src.AnotherSpace.Encrypter import caesar_cipher

@pytest.mark.parametrize(
    ("text", "shift", "expected"),
    [
        ("Hello World", 1, "Ifmmp Xpsme"),
        ("Test", 33, "Alza")
    ]
)
def test_caesar_cipher(text: str, shift: int, expected: str):
    result = caesar_cipher(text, shift)

    assert result == expected
