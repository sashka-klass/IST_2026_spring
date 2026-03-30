import typing as tp


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            # Определяем базовую позицию
            if char.isupper():
                start = ord('A')
            else:
                start = ord('a')
            # Сдвигаем букву
            shifted_char = chr((ord(char) - start + shift) % 26 + start)
            ciphertext += shifted_char
        else:
            ciphertext += char
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            if char.isupper():
                start = ord('A')
            else:
                start = ord('a')
            # Дешифруем: вычитаем сдвиг
            shifted_char = chr((ord(char) - start - shift) % 26 + start)
            plaintext += shifted_char
        else:
            plaintext += char
    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    Пробует все возможные сдвиги (0-25) и возвращает тот,
    при котором больше всего слов из расшифрованного текста
    есть в словаре.
    
    >>> caesar_breaker_brute_force("sbwkrq", {"python", "java", "c++"})
    3
    """
    best_shift = 0
    best_count = 0
    
    # Пробуем все возможные сдвиги от 0 до 25
    for shift in range(26):
        # Расшифровываем текст с текущим сдвигом
        decrypted = decrypt_caesar(ciphertext, shift)
        
        # Разбиваем расшифрованный текст на слова
        # (убираем знаки препинания, оставляем только буквы)
        words = []
        current_word = ""
        for char in decrypted:
            if char.isalpha():
                current_word += char.lower()
            else:
                if current_word:
                    words.append(current_word)
                    current_word = ""
        if current_word:
            words.append(current_word)
        
        # Считаем, сколько слов из расшифрованного текста есть в словаре
        count = sum(1 for word in words if word in dictionary)
        
        # Если нашли больше совпадений, запоминаем этот сдвиг
        if count > best_count:
            best_count = count
            best_shift = shift
    
    return best_shift