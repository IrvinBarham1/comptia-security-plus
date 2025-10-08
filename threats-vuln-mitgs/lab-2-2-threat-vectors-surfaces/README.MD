# Lab 2.2 — Attack Vectors & Delivery Methods

## 🎯 Objective
**“Explain common threat vectors and attack surfaces.”**

This section explores how adversaries deliver malicious payloads or gain access to targets using **message-based, network, software, and human vectors.**

---

## 📖 Background

An **attack vector** is the path or method an adversary uses to infiltrate or affect a system.  
Understanding how attacks are delivered helps analysts detect, prevent, and respond to incidents more effectively.

### Categories of Vectors
| Type | Examples |
|:--|:--|
| **Message-based** | Email, SMS (SMiShing), Instant Messaging |
| **Image-based** | Steganography or hidden payloads in media |
| **File-based** | Malicious documents, macros, or scripts |
| **Voice Call** | Vishing / phone-based social engineering |
| **Removable Device** | USB drives, rogue peripherals |
| **Vulnerable Software** | Agent-based vs. agentless flaws |
| **Unsupported Systems** | Legacy apps or OS without patches |
| **Unsecure Networks** | Weak wireless/WEP, exposed wired ports, insecure Bluetooth |
| **Open Service Ports** | Unnecessary or misconfigured services exposed to the internet |
| **Default Credentials & Supply Chain** | Weak vendor defaults, compromised suppliers |
| **Human Vectors / Social Engineering** | Phishing, vishing, smishing, pretexting, impersonation, watering hole, brand impersonation, typosquatting, misinformation/disinformation |

---

## 🧩 MCQ Sets

The `scenarios/` directory includes multiple JSON files for this objective:

Each question is scenario-driven and includes:
- Four plausible multiple-choice answers  
- Correct answer index  
- Examples + short explanations  

---

## ▶️ How to Run

```bash
# Run any quiz set
cd lab-2-2-threat-vectors-surfaces/python
py lab.py

# Example output
Q1:  A user downloads a malicious attachment from an email...
Choices: ['Image-based', 'Email (message-based)', 'File-based', 'Voice call']
Your answer: Email
✅ Correct – Email is a common message-based vector used in phishing attacks.
