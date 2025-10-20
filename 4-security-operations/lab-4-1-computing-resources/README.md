# Lab 4.1 — Security Operations

## 🎯 Objective
**“Given a scenario, apply common security techniques to computing resources.”**

This lab focuses on implementing and validating **secure configurations**, **hardening procedures**, and **protective controls** across a variety of platforms—such as workstations, mobile devices, servers, and cloud infrastructure.  
It also explores **wireless security**, **mobile deployment models**, and **application-level protection** used to safeguard enterprise systems.

---

## 📖 Background

Security techniques help ensure that computing environments remain **confidential, available, and trustworthy**.  
They combine configuration standards, system hardening, and monitoring to reduce attack surfaces.

### Key Concepts

| Category | Description |
|:--|:--|
| **Secure Baselines** | Establish, deploy, and maintain configuration templates that define approved security settings. |
| **Hardening Targets** | Apply least-privilege and disable unnecessary functions across devices such as servers, switches, routers, IoT, and embedded systems. |
| **Wireless Security** | Strengthen Wi-Fi implementations with WPA3, centralized AAA/RADIUS authentication, and site surveys or heat maps to prevent signal leakage. |
| **Mobile Solutions** | Manage smartphones and tablets through MDM and deployment models such as BYOD, COPE, and CYOD to enforce encryption and remote wipe. |
| **Application Security** | Integrate input validation, secure cookies, static code analysis, and code signing into the development lifecycle. |
| **Sandboxing** | Isolate untrusted code or applications to observe behavior without endangering production systems. |
| **Monitoring** | Continuously collect and analyze logs, alerts, and device telemetry for anomaly detection and policy enforcement. |

---

## 🧩 MCQ Sets

The `scenarios/` folder includes JSON-based question sets covering:

- Secure baseline management  
- Hardening of mobile, workstation, network, and cloud systems  
- Wireless installation and protection  
- Mobile device management and deployment models  
- Application-level defenses and sandboxing techniques  

Each scenario provides:
- Four multiple-choice options  
- Correct-answer index  
- Real-world examples and concise explanations  

---

## 🧑‍💻 Lab Tasks

1. **Review the MCQ sets** in the `scenarios/` directory.  
   Each question reinforces security concepts through applied examples.

2. **Run the quiz engine (`lab.py`)** to:  
   - Shuffle and present questions  
   - Accept user input  
   - Score and display real-time feedback  

---

## ▶️ How to Run

**Python:**
```bash
cd lab-4-1-computing-resources/python
py lab.py
