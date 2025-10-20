# Lab 4.3 — Security Operations

## 🎯 Objective
**“Explain various activities associated with vulnerability management.”**

This lab demonstrates the end-to-end process of **identifying, analyzing, remediating, validating, and reporting** vulnerabilities.  
It reinforces how organizations maintain a proactive and repeatable defense posture through continuous assessment and risk-based prioritization.

---

## 📖 Background

Vulnerability management is a **continuous security discipline** that ensures weaknesses are identified and resolved before attackers can exploit them.  
Each phase contributes to the organization’s ability to **reduce risk exposure**, **measure remediation success**, and **communicate results** to leadership.

### Lifecycle Phases and Examples

| Phase | Purpose | Example |
|:--|:--|:--|
| **Identification** | Discover vulnerabilities via scans, penetration tests, and threat-intelligence feeds | Nessus, OpenVAS, OSINT |
| **Analysis** | Validate findings, eliminate false positives, and prioritize using CVSS/CVE | Severity scoring and impact mapping |
| **Remediation & Response** | Apply patches, segmentation, or compensating controls | System patching, ACL hardening |
| **Validation** | Confirm fixes through rescans, audits, and verification testing | Post-remediation scan |
| **Reporting** | Document outcomes, residual risks, and compliance status | Vulnerability summary report |

---

## 🧩 MCQ Sets

The `scenarios/` directory contains JSON question sets that cover every stage of the lifecycle:

- **Identification & Analysis** — vulnerability scans, threat feeds, false positives/negatives, CVSS scoring  
- **Response & Remediation** — patching, insurance, segmentation, compensating controls, exceptions  
- **Validation & Reporting** — rescanning, audit, verification, management reports  

Each question includes multiple-choice options, examples, and concise explanations for self-review.

---

## 🧑‍💻 Lab Tasks

1. **Review the MCQ files** in `scenarios/` to study realistic vulnerability management workflows.  
2. **Run the quiz engine** (`lab.py`) to:  
   - Randomize questions and answers  
   - Accept user input and display feedback  
   - Track and score results in real time  
3. **Optional Hands-On Exercises**   
   - Perform a local vulnerability scan using a tool like OpenVAS or Nmap  
   - Simulate a patch cycle and validate remediation through rescanning  
   - Draft a simple vulnerability report summarizing findings and actions  

---

## ▶️ How to Run

**Python:**
```bash
cd lab-4-3-vulnerability-management/python
py lab.py
