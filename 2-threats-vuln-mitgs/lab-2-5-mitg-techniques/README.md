# Lab 2.5 — Mitigation Techniques

## 🎯 Objective
**“Explain the purpose of mitigation techniques used to secure the enterprise.”**

This lab focuses on practical methods to secure systems, networks, and applications using **preventive, detective, and corrective controls** such as segmentation, access restrictions, patching, and monitoring.

---

## 📖 Background

Mitigation techniques are essential for strengthening an organization’s security posture.  
They represent the tactical measures used to **reduce the likelihood and impact of attacks** through layered defenses and proactive management.

Each technique contributes uniquely to overall resilience:

| Technique | Description |
|:--|:--|
| **Segmentation** | Divides networks and workloads into isolated zones to limit lateral movement. |
| **Access Control (ACLs / Permissions)** | Restricts access to authorized users or traffic. |
| **Application Allow List** | Ensures only trusted software can execute. |
| **Isolation** | Separates sensitive systems or environments to prevent compromise. |
| **Patching** | Updates software to fix vulnerabilities and improve stability. |
| **Encryption** | Protects data confidentiality in transit and at rest. |
| **Monitoring** | Detects suspicious activity and provides situational awareness. |
| **Least Privilege** | Grants users only the permissions necessary for their roles. |
| **Configuration Enforcement** | Maintains secure baselines and prevents unauthorized changes. |
| **Decommissioning** | Securely removes assets and data from service. |

### Hardening Techniques

| Technique | Description |
|:--|:--|
| **Encryption** | Protects data confidentiality through cryptographic algorithms. |
| **Installation of Endpoint Protection** | Detects and prevents malware using antivirus or EDR solutions. |
| **Host-based Firewall** | Filters inbound and outbound connections on the device itself. |
| **Host-based Intrusion Prevention System (HIPS)** | Monitors and blocks malicious host-level activity in real time. |
| **Disabling Ports/Protocols** | Reduces the attack surface by turning off unused network services. |
| **Default Password Changes** | Prevents compromise from well-known vendor credentials. |
| **Removal of Unnecessary Software** | Eliminates unused or risky applications that increase exposure. |

---

## 🧩 MCQ Sets

The `scenarios/` folder contains JSON question sets aligned with this objective.  

Each scenario includes:
- Four **multiple-choice options**  
- The **correct answer index**  
- **Examples** and concise **explanations** for reinforcement  

These MCQs test your ability to identify and apply mitigation techniques in real-world situations.

---

## 🧑‍💻 Lab Tasks

1. **Review the MCQ sets** under `scenarios/`.  
   Each question targets a specific mitigation
   
## ▶️ How to Run

**Python:**
```bash
cd lab-2-5-mitg-techniques/python
py lab.py