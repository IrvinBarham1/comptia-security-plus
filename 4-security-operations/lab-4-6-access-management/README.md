# Lab 4.6 — Security Operations

## 🎯 Objective
**“Given a scenario, implement and maintain identity and access management.”**

This lab develops the ability to **control, verify, and monitor user access** across enterprise systems.  
It demonstrates how effective identity and access management (IAM) reduces insider risk, supports compliance, and enforces the principle of **least privilege** through technologies like **SSO, MFA, PAM, and directory services**.

---

## 📖 Background

Identity and Access Management (IAM) ensures that the **right users have the right access at the right time**.  
Modern IAM programs combine provisioning automation, authentication standards, and access-control models to protect critical systems and data.

### Core Focus Areas

| Category | Purpose | Example Technologies |
|:--|:--|:--|
| **Account Lifecycle Management** | Automate creation, modification, and removal of user accounts | Provisioning, De-provisioning |
| **Access Models & Permissions** | Define who can access resources and how | RBAC, ABAC, DAC, MAC, Least Privilege |
| **Authentication & Federation** | Centralize and extend identity across platforms | LDAP, OAuth, SAML, Federation, SSO |
| **Identity Validation & Assurance** | Verify and maintain trust in user identities | Identity Proofing, Attestation, Interoperability |
| **Multifactor Authentication** | Strengthen verification using multiple factors | Password + Token, Biometric, Security Key |
| **Password & Credential Security** | Enforce strong password practices or eliminate them | Complexity, Age, Managers, Passwordless |
| **Privileged Access Management (PAM)** | Control administrative accounts and sensitive credentials | Just-in-Time, Vaulting, Ephemeral Credentials |

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
cd lab-4-6-access-management/python
py lab.py
