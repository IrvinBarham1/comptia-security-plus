# Lab 1.1 — Security Controls: Categories & Control Types

## 🎯 Objective

**“Compare and contrast various types of security controls.”**

Correctly identify security controls by their **category** and **type**

---

## 📖 Background

Security controls are organized into **categories** and **types**:

### Control Categories
- **Technical** — Enforced by technology (e.g., firewalls, IDS/IPS, encryption)  
- **Managerial** — Policies, standards, and management oversight  
- **Operational** — Processes and procedures carried out by people  
- **Physical** — Tangible barriers such as locks, fences, guards, and surveillance  

### Control Types
- **Preventive** — Stops an incident before it happens  
- **Deterrent** — Discourages malicious activity  
- **Detective** — Identifies and alerts to incidents in progress or after they occur  
- **Corrective** — Restores systems after an incident  
- **Compensating** — Provides alternative protection when a primary control cannot be implemented  
- **Directive** — Provides guidance or requirements (e.g., policies, signage)

---

## 🧑‍💻 Lab Tasks

1. **Review the scenarios** in the `scenarios/` folder (e.g., `set-01.json`).  
   Each scenario lists several controls such as firewall rules, warning banners, or SIEM alerts.

2. **Label each security control question** with:
   - A **category** (Technical, Managerial, Operational, Physical)  
   - A **type** (Preventive, Deterrent, Detective, Corrective, Compensating, Directive)  

3. **Implement a grader logic** (`lab.py`) to:
   - Compare answers against expected mappings in the scenario files  
   - Output a percentage score 

---

## ✅ Acceptance Criteria

- All security controls in `set-01.json` are labeled with a valid **category** and **type**   
- `lab.py` runs successfully and score answers correctly  

---

## 🚀 Stretch Goals

- Create additional scenario files (e.g., `set-02.json`) for practice  

---

## ▶️ How to Run

**Python:**
```bash
cd lab-1-1-security-controls\python
py lab.py
```

--- 

## 📝 Reflection

Shuffling the questions helped me learn the definitions better. 