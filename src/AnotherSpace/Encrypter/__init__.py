

def caesar_cipher(text: str, shift: int) -> str:
    """Encrypt a given text using the Caesar cipher algorithm.

    This function applies the Caesar cipher encryption method to a given text.
    It shifts each alphabetic character by a specified number of positions while
    leaving non-alphabetic characters unchanged.

    Args:
        `text (str)`: The input text to be encrypted.
        `shift (int)`: The number of positions to shift each character by.

    Returns:
        str: The encrypted text.

    Raises:
        ValueError: If the shift value is not an `integer`.

    Example:
        >>> caesar_cipher("Hello, World!", 3)
        'Khoor, Zruog!'
    """

    if not isinstance(shift, int):
        raise ValueError("Shift must be an integer.")

    encrypted_text = ""

    for char in text:
        if char.isalpha():  # Check if the current character is alphabetic.
            position = ord(char)  # Get the ASCII value of the character.

            new_position = position + shift  # Calculate the new position after shifting.

            if char.isupper():
                new_position = (new_position - ord('A')) % 26 + ord('A')  # Adjust within A-Z range.
            else: 
                new_position = (new_position - ord('a')) % 26 + ord('a')  # Adjust within a-z range.

            encrypted_text += chr(new_position)  # Append the encrypted character to the result.
        else:
            encrypted_text += char  # Append non-alphabetic characters as they are.

    return encrypted_text
