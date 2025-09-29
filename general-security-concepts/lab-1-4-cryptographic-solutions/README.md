# Lab 1.4 — Cryptographic Solutions

## 🎯 Objective
**“Given a scenario, implement and configure cryptographic solutions.”**

This lab demonstrates cryptographic fundamentals through:  
- Multiple-choice questions (MCQs) covering PKI, encryption, certificates, and related concepts  
- Hands-on Python coding exercises:
  - Symmetric vs. asymmetric encryption
  - Diffie–Hellman key exchange
  - Mini blockchain immutability

---

## 📖 Background
Cryptography underpins **confidentiality, integrity, authentication, and non-repudiation** in modern security.  

- **Symmetric encryption (AES):** Same key for encryption and decryption, very fast, used for bulk data.  
- **Asymmetric encryption (RSA, ECC):** Uses a keypair (public/private). Slower, but critical for key exchange, digital signatures, and PKI.  
- **Key exchange (Diffie–Hellman):** Two parties establish a shared secret over an insecure channel without sending the secret directly.  
- **Blockchain:** Links blocks with cryptographic hashes to prevent tampering and ensure integrity of transaction history.  
- **Certificates (PKI):** Provide trusted identities and secure communications through certificate authorities (CAs), CRLs, OCSP, and more.  

---

## 📝 Multiple-Choice Question Practice
The `scenarios/` folder includes JSON sets (e.g., `set-01.json`, `set-02.json`, `set-03.json`, `set-04.json`) covering Objective 1.4 topics:  

- **Public Key Infrastructure (PKI):** Public/private keys, key escrow, trust hierarchy  
- **Encryption:** Symmetric, asymmetric, levels of encryption, key exchange, algorithms, key length  
- **Algorithms:** DES, 3DES, AES, Blowfish, Twofish, Rivest Ciphers, RSA, Diffie–Hellman, ECC  
- **Tools:** TPM, HSM, KMS, secure enclave  
- **Obfuscation:** Steganography, tokenization, data masking  
- **Hashing Concepts:** Hashing, salting, key stretching, digital signatures, blockchain, open ledgers  
- **Certificates:** CA, CRL, OCSP, self-signed, third-party, root of trust, CSR, wildcard  

Each question includes:
- A **scenario-based prompt**  
- **Choices** with distractors  
- The **correct answer index**  
- **Examples** and **explanations**  

Run them with the quiz engine (`lab.py`), which:
- Shuffles questions and answers each run  
- Accepts user input  
- Provides feedback and explanations  
- Tracks score and progress  

---

## 🧑‍💻 Lab Tasks

1. **Symmetric vs. Asymmetric**  
   - Implement AES-256 (symmetric) and RSA (asymmetric, hybrid).  
   - Compare correctness and timing to show efficiency differences.  

2. **Key Exchange**  
   - Simulate Diffie–Hellman key exchange.  
   - Both parties derive the same shared private key without transmitting it.  

3. **Blockchain**  
   - Build a sample blockchain where each block links to the previous hash.  
   - Validate the chain.  
   - Demonstrate that tampering with data invalidates the chain.  

---

## ✅ Acceptance Criteria
- MCQs in `set-01.json`, `set-02.json`, `set-03.json`, and `set-04.json` cover all cryptographic objectives.  
- `lab.py` runs successfully, shuffles questions, and scores with feedback.  
- `symmetric_vs_asymmetric_lab.py` demonstrates AES vs. RSA hybrid encryption.  
- `key_exchange_lab.py` produces identical derived keys for two simulated parties.  
- `blockchain_lab.py` builds a valid chain and detects tampering as invalid.  

---

## ▶️ How to Run

```bash
# Run MCQ quiz engine
py lab.py

# Symmetric vs Asymmetric Encryption
py symmetric_vs_aysmmetric_lab.py

>>> Symmetric Encryption AES-256: (True, 0.0009932518005371094)
>>> Asymmetric Encryption RSA (hybrid): (True, 0.001088857650756836)

# Diffie–Hellman Key Exchange
py key_exchange_lab.py
Shared Secret key for a: 37
Shared Secret key for b: 37

# Blockchain Integrity
py blockchain_lab.py

Block 0: 61cb745b419735d59d025a1e80df6b1c0e6ca5c6f809c9dc522a75fce5ddc47b (prev: 0...)
Block 1: 2c58e70de3fc71c880a078b132a553f4dd55fa229fe80bd330140abe59489bc1 (prev: 61cb745b...)
Block 2: c07b4083ee0b7806c423012bef567621a24ace315954381cb5fac3ffd918e53e (prev: 2c58e70d...)
Block 3: 1b8c1bc40f3bcbbd7e4e51da33e9c9a4a57970cb95b9024ec4c583c6820a3d8b (prev: c07b4083...)

Chain valid? :  True
After tampering, chain valid? :  False
```

---

## 📝 Reflection

This lab made the trade-offs in cryptography visible:
-Symmetric = fast, bulk data
-Asymmetric = slower, but enables secure key distribution
-Key exchange = foundation for TLS and VPNs
-Blockchain = illustrates how tamper detection relies on linked hashes
-Certificates = provide trusted identity and revocation mechanism