# Lab 1.2 — Fundamental Security Concepts

## 🎯 Objective

**“Summarize fundamental security concepts.”**

Correctly apply foundational cybersecurity principles such as **CIA, AAA, Gap Analysis, Zero Trust, Physical Security, and Deception/Disruption technologies**.

---

## 📖 Background

This objective reinforces the **core building blocks** of cybersecurity:

### CIA Triad  
- **Confidentiality** — Ensures only authorized users can access information  
- **Integrity** — Ensures data remains accurate and unaltered  
- **Availability** — Ensures systems and data are accessible when needed  

### Non-repudiation  
- Prevents denial of actions, often through **digital signatures** and logging  

### Authentication, Authorization, and Accounting (AAA)  
- **Authentication** — Verifies identity (who you are)  
- **Authorization** — Determines what you can access  
- **Accounting** — Tracks and logs user activity  

### Gap Analysis  
- Compares current vs. desired state to identify shortfalls  
- Includes **Technical Gap Analysis**, **Business Gap Analysis**, and **Plan of Action & Milestones (POA&M)**  

### Zero Trust Architecture  
- **Never trust, always verify**  
- **Control Plane**: adaptive identity, threat scope reduction, policy-driven access, policy admin/engine  
- **Data Plane**: implicit trust zones, subject/system, policy enforcement point  

### Physical Security  
- Barriers (bollards, fencing)  
- Controlled access (vestibules, badges, guards)  
- Surveillance (CCTV, lighting)  
- Sensors (infrared, pressure, microwave, ultrasonic)  

### Deception & Disruption Technology  
- **Honeypot** — Decoy system  
- **Honeynet** — Network of honeypots  
- **Honeyfile** — Decoy document  
- **Honeytoken** — Decoy credential/data  

---

## 🧑‍💻 Lab Tasks

1. **Review the questions** in the `scenarios/` folder (e.g., `set-01.json`).  
   Each question tests a specific concept under Objective 1.2.  

2. **Answer each question** in multiple-choice format.  
   - Questions are shuffled on each run for variety  
   - After each answer, the program shows **examples** and **explanations**  

3. **Run the quiz engine** (`lab.py`) to:  
   - Present questions and choices  
   - Accept user input  
   - Score and display progress  

4. **Hash Check Integrity**
    - Create `sample.txt` 
    - Use SHA256 hash on file and store digest
    - Change `sample.txt` and validate one byte change alters the hash digest

5. **Honeypot **
    - Run a simple TCP honeypot (`honeypot_lab.py`) that listens on a local port.  
    - When a client connects, it:  
        - Logs the **source IP/port** and any **data sent**  
        - Sends back a **fake HTTP response** (e.g., "Welcome, make yourself at home!")  
        - Appends encrypted entries into `honeypot.log.enc` for analysis  
   - Test it with a browser (`http://127.0.0.1:2222`).  
   - Later, decrypt and review the log entries to observe how requests are captured and recorded.  
---

## ✅ Acceptance Criteria

- At least **20 MCQs** in `set-01.json`, covering every bullet of Objective 1.2  
- `lab.py` runs successfully and provides scoring with feedback  
- Each question includes **examples** and an **explanation** for reinforcement  

---

## 🚀 Stretch Goals

- Add **PBQ-style scenario files** (e.g., role-based access decisions, Zero Trust enforcement examples)  
- Create additional sets (`set-03.json`, `set-04.json`) for spaced repetition  

---

## ▶️ How to Run

**Python:**
```bash
cd lab-1-2-fundamentals\python
# Run the multiple-choice quiz
py lab.py

# Run the hash integrity check
py hash_check_lab.py

# Run the honeypot
py honeypot_lab.py

# Decrypt and review honeypot logs
py log_decrypt.py