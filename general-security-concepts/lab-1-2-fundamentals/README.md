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
py lab.py ..\scenarios\set-01.json --shuffle
