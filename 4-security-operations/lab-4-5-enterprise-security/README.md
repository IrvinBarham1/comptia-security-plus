# Lab 4.5 — Security Operations

## 🎯 Objective
**“Given a scenario, modify enterprise capabilities to enhance security.”**

This lab demonstrates how administrators strengthen enterprise defenses by **configuring network, system, and endpoint capabilities**.  
It focuses on technologies such as **firewalls, IDS/IPS, web filters, NAC, DLP, EDR/XDR, and secure protocol implementations** that collectively improve an organization’s detection and prevention posture.

---

## 📖 Background

Enterprises evolve their security operations by continuously tuning and upgrading core infrastructure.  
Enhancing security capabilities means **optimizing configurations, selecting secure protocols, and deploying advanced monitoring tools** to reduce attack surfaces and enforce defense-in-depth.

### Core Focus Areas

| Category | Purpose | Example Tools & Concepts |
|:--|:--|:--|
| **Network Security Controls** | Manage traffic flow, detect intrusions, and filter malicious content | Firewalls, ACLs, IDS/IPS, Web Filters |
| **Secure Communication & Email** | Protect data in transit and authenticate legitimate senders | HTTPS, SSH, IPSec, DNS Filtering, SPF, DKIM, DMARC |
| **System & Endpoint Hardening** | Enforce OS security policies and endpoint visibility | Group Policy, SELinux, File Integrity Monitoring, EDR/XDR |
| **Data & Access Protection** | Prevent unauthorized data movement and verify device compliance | DLP, NAC, UBA (User Behavior Analytics) |

---

## 🧩 MCQ Sets

1. **Review the MCQ sets** in the `scenarios/` directory.  
   Each scenario tests how security is impacted at different stages of the asset lifecycle.

2. **Run the quiz engine (`lab.py`)** to:
   - Randomize and present questions  
   - Accept user input  
   - Display score and feedback  

## ▶️ How to Run

**Python:**
```bash
cd lab-4-5-enterprise-security/python
py lab.py
