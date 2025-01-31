def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                encrypted_text += chr(((ord(char) - ord('a') + shift_amount) % 26) + ord('a'))
            else:
                encrypted_text += chr(((ord(char) - ord('A') + shift_amount) % 26) + ord('A'))
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    return encrypt(text, -shift)

# Example usage:
encrypted = encrypt("Python Task,!", 5)
print(encrypted)  # Output: "Udymts Yfxp,!"
decrypted = decrypt(encrypted, 5)
print(decrypted)  # Output: "Python Task,!"