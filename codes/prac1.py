# CEASAR CIPHER CRYPTOGRAPHY

def encrypt(text, s):

    result = ''

    for i in range(len(text)):
        char = text[i]

        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
        else:
            result += chr((ord(char) + s-97) % 26 + 97)

    return result

text = input("Enter the text to encrypt: ")
s = 3
print("Text: " + text)
str(s)
print("Cipher: " + encrypt(text, s))

# Transposition cipher: Columnar Transposition Cipher

def transposition_encrypt(plaintext, key):
    # Remove spaces and prepare the grid
    plaintext = plaintext.replace(" ", "")
    cipher_text = [''] * key
    
    for column in range(key):
        pointer = column
        while pointer < len(plaintext):
            cipher_text[column] += plaintext[pointer]
            pointer += key
    
    return ''.join(cipher_text)

def transposition_decrypt(ciphertext, key):
    num_of_columns = int(len(ciphertext) / key)
    num_of_rows = key
    num_of_shaded_boxes = (num_of_columns * num_of_rows) - len(ciphertext)
    
    plain_text = [''] * num_of_columns
    column, row = 0, 0
    
    for symbol in ciphertext:
        plain_text[column] += symbol
        column += 1
        
        if (column == num_of_columns) or (column == num_of_columns - 1 and row >= num_of_rows - num_of_shaded_boxes):
            column = 0
            row += 1
    
    return ''.join(plain_text)

# Example usage
plaintext = "hello world"
key = 5
ciphertext = transposition_encrypt(plaintext, key)
print(f"Transposition Encrypted: {ciphertext}")
decrypted_text = transposition_decrypt(ciphertext, key)
print(f"Transposition Decrypted: {decrypted_text}")
