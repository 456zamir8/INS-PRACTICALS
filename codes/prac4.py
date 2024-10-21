'''Implement digital signature algorithm suc as RSA-based signatures, and verify the integrity 
and authenticity of digitally signed messages'''

from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.Cipher import PKCS1_OAEP
import binascii
from colorama import init, Fore

init(autoreset = True)

# private and public key generation
keyPair = RSA.generate(2048)
pubKey = keyPair.publickey()

# Export keys in PEM format
pubKeyPEM = pubKey.exportKey()
privKeyPEM = keyPair.exportKey()

# Print the public and private key in PEM format
print(Fore.YELLOW + "Public Key PEM Format:")
print(pubKeyPEM.decode('ascii'))

print(Fore.YELLOW + "\nPrivate Key PEM Format:")
print(privKeyPEM.decode('ascii'))

message = b"hello zamir"

# Simulate an altered message after signing
altered_message = b"hello zamir" 

# Hash the message using SHA-256
hash_msg = SHA256.new(message)

# Sign the message hash using the private key
signature = pkcs1_15.new(keyPair).sign(hash_msg)
print(Fore.YELLOW + "\nSignature (hex):", binascii.hexlify(signature).decode())

# Verification process
def verify_signature(pub_key, message, signature):
    try:
        # Recreate the hash of the message
        hash_msg = SHA256.new(message)
        # Verify the signature using the public key
        pkcs1_15.new(pub_key).verify(hash_msg, signature)
        return True
    except (ValueError, TypeError):
        return False

# Simulate message integrity verification
# (The receiver verifies the message using the public key)
is_valid = verify_signature(pubKey, altered_message, signature)

if is_valid:
    print(Fore.GREEN + "\nSignature is valid. The message is authentic and unaltered.")
else:
    print(Fore.RED + "\nSignature is invalid. The message might have been altered or is not authentic.")
