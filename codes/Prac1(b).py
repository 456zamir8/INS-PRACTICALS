# Substitution cipher: Caesar Cipher (Shift-based)
def substitution_encrypt(plaintext, shift):
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():  # Encrypt only alphabetic characters
            shift_base = ord('a') if char.islower() else ord('A')
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char  # Non-alphabet characters remain unchanged
    return encrypted_text

def substitution_decrypt(ciphertext, shift):
    return substitution_encrypt(ciphertext, -shift)  # Decrypt by shifting in the opposite direction

# Transposition cipher with padding
def transposition_encrypt(plaintext, key):
    # Remove spaces and prepare the grid
    plaintext = plaintext.replace(" ", "")
    padding_char = 'X'
    # Pad the plaintext if necessary
    if len(plaintext) % key != 0:
        plaintext += padding_char * (key - len(plaintext) % key)
    
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
    
    # Remove any padding characters
    return ''.join(plain_text).rstrip('X')

# Combined encryption and decryption
def combined_encrypt(plaintext, shift, key):
    # Step 1: Apply substitution cipher (Caesar)
    substituted_text = substitution_encrypt(plaintext, shift)
    
    # Step 2: Apply transposition cipher
    final_encryption = transposition_encrypt(substituted_text, key)
    
    return final_encryption

def combined_decrypt(ciphertext, shift, key):
    # Step 1: Apply transposition decryption
    transposed_text = transposition_decrypt(ciphertext, key)
    
    # Step 2: Apply substitution decryption
    final_decryption = substitution_decrypt(transposed_text, shift)
    
    return final_decryption

# Example usage
plaintext = "This is ins practical"
shift = 2
key = 5
ciphertext = combined_encrypt(plaintext, shift, key)
print(f"Original Message: {plaintext}")
print(f"Combined Encrypted: {ciphertext}")
decrypted_text = combined_decrypt(ciphertext, shift, key)
print(f"Combined Decrypted: {decrypted_text}")
