import time
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
#import rsa
from os import urandom

MESSAGE = b"Coding is fun, I hope it is for you!"

def symmetric_algorithm():
    # AES-256
    key = urandom(32)
    # Initialization Vector - prevents same text generating same encryption
    iv = urandom(16)

    cipher = Cipher(algorithms.AES256(key), modes.CFB(iv))
    
    start = time.time()
    ciphertext = cipher.encryptor().update(MESSAGE) + cipher.encryptor().finalize()
    decrypted = cipher.decryptor().update(ciphertext) + cipher.decryptor().finalize()
    elapsed = time.time() - start
    
    return decrypted == MESSAGE, elapsed

def aysmmetric_algorithm():
    #RSA
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()
    
    start = time.time()
    ciphertext = public_key.encrypt(
        MESSAGE,
        padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
    )
    decrypted = private_key.decrypt(
        ciphertext,
        padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
    )
    elapsed = time.time() - start

    return decrypted == MESSAGE, elapsed



def main():
    print(f">>> Symmetric Encryption AES-256: {symmetric_algorithm()}")
    print(f">>> Aysmmetric Encryption RSA: {aysmmetric_algorithm()}")

if __name__ == "__main__":
    main()