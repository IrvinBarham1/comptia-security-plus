# Lab 4.9 — Security Operations

## 🎯 Objective
**“Given a scenario, use data sources to support an investigation.”**

This lab focuses on how **security analysts collect, analyze, and correlate data** from multiple sources to investigate incidents.  
It emphasizes the role of logs, dashboards, and automated reports in identifying patterns, confirming compromises, and supporting forensic findings.

---

## 📖 Background

Every security investigation relies on accurate and comprehensive data.  
Analysts use log files, vulnerability reports, dashboards, and packet captures to **reconstruct attacker activity** and validate alerts.  
Combining these data sources enhances visibility and improves the accuracy of root cause analysis.

### Core Focus Areas

| Category | Purpose | Example Technologies |
|:--|:--|:--|
| **Log Data** | Identify, correlate, and trace suspicious activities | Firewall, Application, Endpoint, OS, IDS/IPS, Network, Metadata |
| **Data Sources** | Provide broader operational and vulnerability context | Vulnerability Scans, Automated Reports, Dashboards, Packet Captures |

---

## 🧩 MCQ Sets

1. **Review the MCQ sets** in the `scenarios/` directory.  
   Each scenario tests how different data sources are used to confirm, analyze, and support security investigations.

2. **Run the quiz engine (`lab.py`)** to:
   - Randomize and present questions  
   - Accept user input  
   - Display score and feedback  

---

## ▶️ How to Run

**Python:**
```bash
cd lab-4-9-support-investigation/python
py lab.py
