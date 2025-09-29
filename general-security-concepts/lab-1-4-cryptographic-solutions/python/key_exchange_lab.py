import secrets, hashlib

# Diffie-Hellman Key Exchange

def power(a, b, P):
    if b == 1:
        return a
    else:
        return (a ** b) % P

# Public Parameters
P = 45 
G = 7

# Private Keys
a = 3
b = 7

# Generate Public Keys
x = power(G, a, P)
y = power(G, b, P)

# Exchange Public Keys and Generate Private Keys
key_a = power(y, a, P)
key_b = power (x, b, P)

print(f"Shared Secret key for a: {key_a}")
print(f"Shared Secret key for b: {key_b}")