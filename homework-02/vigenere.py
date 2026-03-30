def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    key_index = 0
    for char in plaintext:
        if char.isalpha():
            # Определяем сдвиг по букве ключа
            shift = ord(keyword[key_index % len(keyword)].lower()) - ord('a')
            if char.isupper():
                # Для заглавных букв
                encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                # Для строчных букв
                encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            ciphertext += encrypted_char
            key_index += 1
        else:
            ciphertext += char
    return ciphertext

def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    key_index = 0
    for char in ciphertext:
        if char.isalpha():
            # Определяем сдвиг по букве ключа
            shift = ord(keyword[key_index % len(keyword)].lower()) - ord('a')
            if char.isupper():
                # Для заглавных букв
                decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                # Для строчных букв
                decrypted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            plaintext += decrypted_char
            key_index += 1
        else:
            plaintext += char
    return plaintext