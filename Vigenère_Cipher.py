def is_uppercase(c):
    return 'A' <= c <= 'Z'

def is_lowercase(c):
    return 'a' <= c <= 'z'

def is_letter(c):
    return is_uppercase(c) or is_lowercase(c)

def filter_key(key):
    result = []
    for ch in key:
        if is_letter(ch):
            if is_uppercase(ch):
                result.append(ord(ch) - ord('A'))
            elif is_lowercase(ch):
                result.append(ord(ch) - ord('a'))
    return result

def crypt(input_text, key_array, is_decrypt):
    output = []
    j = 0

    if is_decrypt:
        key_array = [(26 - k) % 26 for k in key_array]

    for ch in input_text:
        if is_uppercase(ch):
            encrypted_char = chr((ord(ch) - ord('A') + key_array[j % len(key_array)]) % 26 + ord('A'))
            output.append(encrypted_char)
            j += 1
        elif is_lowercase(ch):
            encrypted_char = chr((ord(ch) - ord('a') + key_array[j % len(key_array)]) % 26 + ord('a'))
            output.append(encrypted_char)
            j += 1
        else:
            output.append(ch)

    return ''.join(output)

def main():
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").upper()
    text = input("Enter the text: ")
    key = input("Enter the key: ")

    if len(key) == 0:
        print("Key is empty")
        return

    key_array = filter_key(key)

    if len(key_array) == 0:
        print("Key has no letters")
        return

    if choice == 'E':
        result = crypt(text, key_array, is_decrypt=False)
        print(f"Encrypted Text: {result}")
    elif choice == 'D':
        result = crypt(text, key_array, is_decrypt=True)
        print(f"Decrypted Text: {result}")
    else:
        print("Invalid choice. Please select 'E' for Encrypt or 'D' for Decrypt.")

if __name__ == "__main__":
    main()
