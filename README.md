# CompTIA Security+ Certification Exam Preparation

These are my own coding exercises I developed to help prepare for the **CompTIA Security+ (SY0-701)** certification exam.  

Each lab is an exercise I built to translate exam objectives into **hands-on, code-driven exercises**. This approach reinforces my exam preparation while also showcasing practical cybersecurity and programming skills.

---

## 📊 Exam Domain Alignment

This project is structured around the official Security+ (SY0-701) objectives:

- **General Security Concepts (12%)**  
  Core principles of security, authentication, and encryption fundamentals.

- **Threats, Vulnerabilities, and Mitigations (22%)**  
  Attack types, social engineering, malware, and defensive strategies.

- **Security Architecture (18%)**  
  Secure system and network design, segmentation, PKI, and cloud security models.

- **Security Operations (28%)**  
  Monitoring, logging, patching, backup/recovery, and incident response procedures.

- **Security Program Management and Oversight (20%)**  
  Governance, risk, and compliance practices, including risk registers, policy development, vendor management, and program oversight.

---

## 📂 Repository Structure

security-plus-labs/
├─ /general-security-concepts
│ ├─ password_policy/ # Lockout & hashing demonstration
│ └─ pki_tls_handshake/ # TLS handshake simulation
├─ /threats-vulns-mitigations
│ ├─ phishing_detector/ # Social engineering classifier
│ ├─ watering_hole_sim/ # Attack + mitigation demo
│ └─ vuln_scan_triage/ # Vulnerability prioritization
├─ /security-architecture
│ ├─ network_segmentation_lab/ # Subnet isolation demo
│ └─ cert_chain_validator/ # Revocation checks (CRL/OCSP)
├─ /security-operations
│ ├─ siem_log_rules/ # Log parsing & detection rules
│ ├─ patch_pipeline/ # Patch > rescan > verify workflow
│ └─ backup_restore_bia/ # Backup & recovery testing
└─ /security-program-mgmt
├─ risk_register/ # Risk lifecycle & ALE/SLE calculations
└─ vendor_risk_review/ # SLA/MOU/NDA analyzer

---


