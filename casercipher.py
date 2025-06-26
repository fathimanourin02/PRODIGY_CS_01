def caesar_encrypt(message, shift):
    encrypted = ""
    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted += chr((ord(char) - base + shift) % 26 + base)
        else:
            encrypted += char
    return encrypted

def caesar_decrypt(message, shift):
    return caesar_encrypt(message, -shift)

def main():
    print("=== Caesar Cipher Encryption and Decryption ===")
    message = input("Enter your message: ")
    
    try:
        shift = int(input("Enter shift value (e.g., 3): "))
    except ValueError:
        print("Invalid input! Shift must be an integer.")
        return

    encrypted = caesar_encrypt(message, shift)
    decrypted = caesar_decrypt(encrypted, shift)

    print("\n--- Results ---")
    print("Original Message :", message)
    print("Encrypted Message:", encrypted)
    print("Decrypted Message:", decrypted)

if __name__ == "__main__":
    main()
