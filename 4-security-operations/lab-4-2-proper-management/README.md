# Lab 4.2 — Security Operations

## 🎯 Objective
**“Explain the security implications of proper hardware, software, and data asset management.”**

This lab focuses on the **lifecycle management of assets** — from acquisition to disposal — and how each stage affects the security, integrity, and accountability of organizational resources.

---

## 📖 Background

Every device, application, and data source represents a potential security risk if not properly tracked and managed.  
A mature asset management process ensures **visibility, accountability, and compliance** across the entire lifecycle.

### Key Lifecycle Stages

| Stage | Description |
|:--|:--|
| **Acquisition / Procurement** | Ensures that new hardware and software are vetted for compliance, trusted vendors, and secure configurations before purchase. |
| **Assignment / Accounting** | Tracks asset ownership, establishes accountability, and applies appropriate classification levels (e.g., public, internal, confidential). |
| **Monitoring / Tracking** | Maintains visibility through inventory databases, automated discovery, and network enumeration to detect unauthorized devices or software. |
| **Disposal / Decommissioning** | Securely removes data and hardware through sanitization, destruction, certification, and retention policies that meet compliance requirements. |

---

## 🧩 MCQ Sets

The `scenarios/` folder contains multiple-choice question sets covering:
- Secure procurement practices  
- Ownership and classification policies  
- Asset tracking and enumeration processes  
- Secure data disposal, destruction, and certification procedures  

Each question includes:
- Four answer options  
- Correct answer index  
- Examples and concise explanations  

---

## 🧑‍💻 Lab Tasks

1. **Review the MCQ sets** in the `scenarios/` directory.  
   Each scenario tests how security is impacted at different stages of the asset lifecycle.

2. **Run the quiz engine (`lab.py`)** to:
   - Randomize and present questions  
   - Accept user input  
   - Display score and feedback  

---

## ▶️ How to Run

**Python:**
```bash
cd lab-4-2-asset-management/python
py lab.py
