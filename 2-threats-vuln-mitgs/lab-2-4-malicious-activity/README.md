# Lab 2.4 — Malicious Activity

## 🎯 Objective
**“Given a scenario, analyze indicators of malicious activity.”**

This section explores how adversaries exploit systems, users, and networks through **malware, physical, network, application, cryptographic, and password-based attacks** — and how to recognize their **indicators of compromise (IoCs)**.

---

## 📖 Background

Cyberattacks vary in motive, sophistication, and delivery method.  
Understanding attack types and their behavioral indicators helps defenders quickly **detect, contain, and respond** to security incidents.

### Attack Classifications

| Category | Common Examples |
|:--|:--|
| **Malware Attacks** | Ransomware, Trojan, Worm, Spyware, Bloatware, Virus, Keylogger, Logic Bomb, Rootkit |
| **Physical Attacks** | Brute-force keypad attempts, RFID cloning, environmental (heat, humidity, power loss) |
| **Network Attacks** | DDoS (amplified/reflected), DNS poisoning, wireless (evil twin), on-path (MITM), credential replay, malicious code |
| **Application Attacks** | Injection, buffer overflow, replay, privilege escalation, forgery, directory traversal |
| **Cryptographic Attacks** | Downgrade, collision, birthday attacks |
| **Password Attacks** | Spraying, brute-force |
| **Indicators of Compromise** | Account lockouts, concurrent sessions, impossible travel, missing or out-of-cycle logs, resource consumption/inaccessibility, documented threat indicators |

---

## 🧩 MCQ Sets

The `scenarios/` directory contains several JSON files aligned to this objective:

Each question includes:
- A **realistic attack scenario**  
- Four plausible multiple-choice answers  
- **Examples** and concise **explanations**  

---

## 🧑‍💻 Lab Concepts

1. **Simulated Malware Chain**  
   - Review JSON question sets simulating ransomware, Trojans, and logic bombs.  
   - Identify key signatures and behaviors for each malware family.  

2. **DDoS Amplification Visualization**  
   - Use a local Python script to simulate reflection/amplification traffic volumes.  

3. **SQL Injection Test**  
   - Create a safe mock API that shows how unsanitized inputs alter queries.  

---

## ▶️ How to Run

```bash
# Navigate to the lab folder
cd lab-2-4-malicious-activity/python

# Run the quiz engine
py lab.py

# Example output
Q1:  A user reports that files are encrypted and a ransom note appears...
Choices: ['Worm', 'Ransomware', 'Trojan', 'Spyware']
Your answer: Ransomware
✅ Correct – Ransomware encrypts data and demands payment for recovery.

Score: 1 / 1 (100%)