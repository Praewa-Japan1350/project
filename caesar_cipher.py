def caesarCipher(s, k):
    result = ""
    k = k % 26

    for char in s:
        if char.islower():
            shifted = (ord(char) - ord("a") + k) % 26
            result += chr(shifted + ord("a"))

        elif char.isupper():
            shifted = (ord(char) - ord("A") + k) % 26
            result += chr(shifted + ord("A"))

        else:
            result += char

    return result
