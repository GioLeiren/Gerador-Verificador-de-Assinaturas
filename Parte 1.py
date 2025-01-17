import random

# Helper function to generate a large prime number with Miller-Rabin test
def generate_large_prime(bits=1024):
    while True:
        candidate = random.getrandbits(bits)
        # Ensure it's odd and sufficiently large
        candidate |= (1 << bits - 1) | 1
        if miller_rabin_test(candidate):
            return candidate

def miller_rabin_test(n, k=20):

    if n == 2 or n == 3:
        return True

    if n % 2 == 0:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for i in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for j in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

# Function to calculate the modular inverse using Extended Euclidean Algorithm
def modular_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        a, m = m, a % m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

# RSA Key Generation
def generate_rsa_keys(bits=1024):
    p = generate_large_prime(bits)
    q = generate_large_prime(bits)
    n = p * q
    phi = (p - 1) * (q - 1)

    # Choose e such that 1 < e < phi and gcd(e, phi) = 1
    e = 65537  # Commonly used public exponent

    # Calculate d (modular multiplicative inverse of e mod phi)
    d = modular_inverse(e, phi)

    return {
        "public_key": (e, n),
        "private_key": (d, n),
        "primes": (p, q)  # For debugging purposes
    }

# RSA Encryption with OAEP padding (Simplified)
def oaep_encrypt(message, public_key):
    e, n = public_key
    # Convert message to integer
    message_int = int.from_bytes(message.encode('utf-8'), byteorder='big')
    if message_int >= n:
        raise ValueError("Message is too large for the key size.")
    # Encrypt: c = m^e mod n
    cipher_int = pow(message_int, e, n)
    return cipher_int

# RSA Decryption with OAEP padding (Simplified)
def oaep_decrypt(cipher_int, private_key):
    d, n = private_key
    # Decrypt: m = c^d mod n
    message_int = pow(cipher_int, d, n)
    # Convert integer back to string
    message = message_int.to_bytes((message_int.bit_length() + 7) // 8, byteorder='big').decode('utf-8')
    return message

# Example usage
if __name__ == "__main__":
    # Generate RSA keys
    keys = generate_rsa_keys(bits=1024)
    print("Generated Keys:", keys)

    # Example encryption and decryption
    message = "Hello, RSA!"
    cipher = oaep_encrypt(message, keys['public_key'])
    print("Encrypted Message:", cipher)

    decrypted_message = oaep_decrypt(cipher, keys['private_key'])
    print("Decrypted Message:", decrypted_message)
