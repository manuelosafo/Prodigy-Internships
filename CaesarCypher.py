def encrypt(text, shift):
    result = ""
    # traverse text
    for i in range(len(text)):
        char = text[i]
        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        # Leave non-alphabetical characters unchanged
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    while True:
        choice = input("Enter 'e' to encrypt, 'd' to decrypt, or 'q' to quit: ").lower()
        if choice == 'q':
            print("Goodbye!")
            break
        elif choice in ['e', 'd']:
            text = input("Enter your message: ")
            try:
                shift = int(input("Enter the shift value: "))
            except ValueError:
                print("Please enter a valid integer for the shift value.")
                continue

            if choice == 'e':
                encrypted_text = encrypt(text, shift)
                print(f"Encrypted text: {encrypted_text}")
            elif choice == 'd':
                decrypted_text = decrypt(text, shift)
                print(f"Decrypted text: {decrypted_text}")
        else:
            print("Invalid choice. Please enter 'e', 'd', or 'q'.")

if __name__ == "__main__":
    main()
