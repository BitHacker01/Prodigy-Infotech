letters = 'abcdefghijklmnopqrstuvwxyz'
num_letters = len(letters)

def encrypt(plaintext, key):
    ciphertext = ''
    for letter in plaintext:
        if letter.isalpha():  # Check if the character is a letter
            letter_lower = letter.lower()
            index = letters.find(letter_lower)
            new_index = (index + key) % num_letters
            new_letter = letters[new_index]
            # Preserve the case
            if letter.isupper():
                new_letter = new_letter.upper()
            ciphertext += new_letter
        else:
            ciphertext += letter  # Non-alphabetic characters are added unchanged
    return ciphertext

def decrypt(ciphertext, key):
    plaintext = ''
    for letter in ciphertext:
        if letter.isalpha():  # Check if the character is a letter
            letter_lower = letter.lower()
            index = letters.find(letter_lower)
            new_index = (index - key) % num_letters
            new_letter = letters[new_index]
            # Preserve the case
            if letter.isupper():
                new_letter = new_letter.upper()
            plaintext += new_letter
        else:
            plaintext += letter  # Non-alphabetic characters are added unchanged
    return plaintext

print()
print('***** CAESAR CIPHER PROGRAM *****')
print()

user_input = input('Do you want to encrypt or decrypt? (e/d): ').lower()
print()

if user_input == 'e':
    print('ENCRYPTION MODE SELECTED')
    print()
    key = int(input('Enter the key (1 through 26): '))
    text = input('Enter the text to encrypt: ')
    ciphertext = encrypt(text, key)
    print(f'CIPHERTEXT: {ciphertext}')

elif user_input == 'd':
    print('DECRYPTION MODE SELECTED')
    print()
    key = int(input('Enter the key (1 through 26): '))
    text = input('Enter the text to decrypt: ')
    plaintext = decrypt(text, key)
    print(f'PLAINTEXT: {plaintext}')
else:
    print('Invalid input. Please choose "e" to encrypt or "d" to decrypt.')