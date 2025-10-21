# Lab 4.4 — Security Operations

## 🎯 Objective
**“Explain security alerting and monitoring concepts and tools.”**

This lab strengthens your ability to **detect, analyze, and respond** to abnormal activity across enterprise environments.  
It emphasizes how continuous monitoring, alert correlation, and automation through tools like **SIEM, SCAP, DLP, and NetFlow** enable early detection and faster response to security threats.

---

## 📖 Background

Modern organizations rely on **continuous visibility** into their computing resources.  
Security operations teams collect logs, tune alerts, and automate analysis to recognize anomalies before they become incidents.  
A mature alerting and monitoring strategy improves **incident response times**, maintains **regulatory compliance**, and **reduces risk exposure**.

### Core Focus Areas

| Category | Purpose | Example Tools |
|:--|:--|:--|
| **Monitoring Computing Resources** | Observe performance and security events across systems, applications, and infrastructure | Cloud telemetry, host metrics, uptime dashboards |
| **Alerting and Validation Activities** | Generate, tune, and verify alerts through scanning, quarantine, and remediation workflows | SIEM correlation, EDR isolation, vulnerability scanning |
| **Security Monitoring Tools** | Automate, detect, and prevent incidents using enterprise security technologies | SCAP, Benchmarks, SNMP traps, DLP, NetFlow, Vulnerability Scanners |

---

## 🧩 MCQ Sets

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
cd lab-4-4-alerting-monitoring/python
py lab.py
