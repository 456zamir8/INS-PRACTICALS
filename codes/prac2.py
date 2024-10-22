# RSA ENCRYPTION 
# pip install pycryptodome
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

# Generate RSA key pair (private and public)
keyPair = RSA.generate(1024)
pubKey = keyPair.publickey()

# Extract and print public key components
n = hex(pubKey.n)
e = hex(pubKey.e)
print("Public Key: ")
print(n)
print(e)

# Export public key in PEM format
pubKeyPEM = pubKey.exportKey()
print("\nPublic Key PEM Format:")
print(pubKeyPEM.decode('ascii'))

# Extract and print private key components
d = hex(keyPair.d)
print("\nPrivate Key: ")
print(n)  # n is the same as in the public key
print(d)

# Export private key in PEM format
privKeyPEM = keyPair.exportKey()
print("\nPrivate Key PEM Format:")
print(privKeyPEM.decode('ascii'))

# Message to encrypt
omsg = input("Enter message u want to Encrypt: ")
msg = omsg.encode()  # Correct encoding of the original message

# Encrypt the message with the public key using PKCS1_OAEP
encryptor = PKCS1_OAEP.new(pubKey)
encrypted = encryptor.encrypt(msg)
result = binascii.hexlify(encrypted)
print("\nEncrypted Message (hex):")
print(result)

# Decrypt the message using the private key
decryptor = PKCS1_OAEP.new(keyPair)
decrypted = decryptor.decrypt(encrypted)
print("\nDecrypted Message:")
print(decrypted.decode('utf-8'))
