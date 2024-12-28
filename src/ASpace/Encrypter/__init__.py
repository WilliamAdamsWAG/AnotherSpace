

def caesar_cipher(text, shift):
    encrypted_text = ""
    
    for char in text:
        if char.isalpha():
            position = ord(char)

            new_position = position + shift

            if char.isupper():
                new_position = (new_position - ord('A')) % 26 + ord('A')
            else:
                new_position = (new_position - ord('a')) % 26 + ord('a')

            encrypted_text += chr(new_position)
        else:

            encrypted_text += char

    return encrypted_text
