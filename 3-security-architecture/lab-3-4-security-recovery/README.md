# Lab 3.4 — Resilience and Recovery in Security Architecture

## 🎯 Objective
**“Explain the importance of resilience and recovery in security architecture.”**

This lab explores key principles that ensure business continuity and minimize downtime after disruptions.  
It focuses on redundancy, fault tolerance, backups, power protection, and testing strategies that sustain availability in enterprise environments.

---

## 📖 Background

Resilience in cybersecurity is the **ability to maintain essential functions during and after an incident**.  
Recovery ensures that systems can return to a secure, operational state quickly.

| Concept | Description |
|:--|:--|
| **High Availability** | System design ensuring minimal downtime and continuous operations. |
| **Load Balancing** | Distributes traffic among multiple servers to prevent overload and maintain performance. |
| **Clustering** | Combines multiple systems to act as one, providing redundancy if one node fails. |
| **Site Redundancy** | Uses hot, warm, and cold sites to enable recovery after disasters. |
| **Backup & Replication** | Protects data integrity and allows restoration after loss or corruption. |
| **Power Protection** | Generators and UPS systems prevent downtime due to electrical failures. |
| **Testing and Validation** | Exercises like simulations and failovers confirm readiness before real incidents. |

---

## 🧩 MCQ Sets

The `scenarios/` folder contains JSON-based multiple-choice sets covering:
- **High availability & clustering**
- **Site recovery & redundancy**
- **Backup and power protection**
- **Testing and continuity procedures**

Each question includes:
- Four answer choices  
- A correct answer index  
- Examples and concise explanations  

---

## 🧑‍💻 Lab Tasks

1. **Review the MCQ sets** under `scenarios/`.  
   Each question tests your understanding of resilience, continuity, and recovery strategies.

2. **Run the quiz engine** (`lab.py`) to:  
   - Randomize and present questions  
   - Accept user input  
   - Provide scoring and feedback  

3. **Hands-On Mini Tasks**
   - Simulate a **Load Balancing Test**: Use round-robin logic to distribute fake network requests between two servers.
   - Test a **Failover Concept**: Run a secondary Python thread to emulate backup server response when the primary fails.

---

## ▶️ How to Run

**Python:**
```bash
cd lab-3-4-security-recovery/python
py lab.py
