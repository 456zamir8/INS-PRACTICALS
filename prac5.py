# DEFFIE-HELLMAN KEY EXCHNAGE ALGORITHM
import random

def generate_prime():
    """Generate a large prime number (for demonstration purposes, a small prime is used)."""
    # In practice, use a library for generating large primes.
    return 23  # A small prime for simplicity

def generate_generator(p):
    """Choose a generator (primitive root) for the prime."""
    return 5  # A small generator for demonstration

def generate_private_key():
    """Generate a private key (random number)."""
    return random.randint(1, 10)  # Small range for simplicity

def compute_public_key(private_key, g, p):
    """Compute public key using private key, base (g), and prime (p)."""
    return pow(g, private_key, p)  # g^private_key mod p

def compute_shared_secret(other_public_key, private_key, p):
    """Compute shared secret using the other party's public key and own private key."""
    return pow(other_public_key, private_key, p)  # other_public_key^private_key mod p

# Step 1: Agree on a large prime number and a generator
p = generate_prime()
g = generate_generator(p)

# Step 2: Generate private keys for Alice and Bob
alice_private_key = generate_private_key()
bob_private_key = generate_private_key()

# Step 3: Compute public keys
alice_public_key = compute_public_key(alice_private_key, g, p)
bob_public_key = compute_public_key(bob_private_key, g, p)

# Step 4: Exchange public keys (simulated by direct variable assignment here)
# In practice, this would happen over an insecure channel.
print(f"Alice's Public Key: {alice_public_key}")
print(f"Bob's Public Key: {bob_public_key}")

# Step 5: Compute the shared secret
alice_shared_secret = compute_shared_secret(bob_public_key, alice_private_key, p)
bob_shared_secret = compute_shared_secret(alice_public_key, bob_private_key, p)

# Display the shared secrets
print(f"Alice's Shared Secret: {alice_shared_secret}")
print(f"Bob's Shared Secret: {bob_shared_secret}")

# Verify that both shared secrets are the same
if alice_shared_secret == bob_shared_secret:
    print("Shared secrets match! Key exchange successful.")
else:
    print("Shared secrets do not match! Key exchange failed.")
 
# use it when u want to show the invalid key 
'''invalid_private_key = -1

try:
    alice_public_key_invalid = compute_public_key(invalid_private_key, g, p)
    print(f"\nAlice's Public Key (Invalid): {alice_public_key_invalid}")
finally:
    print("Error while computing public key with invalid private key")'''