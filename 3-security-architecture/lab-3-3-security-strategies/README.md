# Lab 3.3 — Security Architecture

## 🎯 Objective
**“Compare and contrast concepts and strategies to protect data.”**

This lab focuses on identifying, classifying, and protecting data through both **organizational policies** and **technical safeguards**.  
You’ll explore data states, sensitivity levels, and security methods such as encryption, masking, tokenization, and segmentation.

---

## 📖 Background

Organizations handle a wide range of data—each requiring different protection levels based on **sensitivity**, **value**, and **regulatory obligations**.  
Understanding how data is categorized and secured helps ensure confidentiality, integrity, and availability throughout its lifecycle.

### 🗂 Data Types

| Type | Description | Example |
|:--|:--|:--|
| **Regulated** | Governed by external laws or frameworks. | HIPAA-protected medical records |
| **Trade Secret** | Proprietary business information giving competitive advantage. | Manufacturing formula |
| **Intellectual Property** | Creative works or inventions protected by legal rights. | Source code, patents |
| **Legal Information** | Contracts, compliance reports, or court filings. | Regulatory filings |
| **Financial Information** | Transaction, payroll, or account data. | Banking statements |
| **Human- and Non-Human-Readable** | Data designed for people vs. systems. | PDF vs. binary log files |

---

### 🔒 Data Classifications

| Classification | Description | Example |
|:--|:--|:--|
| **Sensitive** | Must be protected from unauthorized disclosure. | Customer PII |
| **Confidential** | Internal-only information. | Internal HR procedures |
| **Public** | Freely available data. | Press releases |
| **Restricted** | Highly sensitive with limited access. | Encryption keys |
| **Private** | Associated with individuals. | Health records, PII |
| **Critical** | Essential for business continuity. | Financial databases |

---

### 🔁 General Data Considerations

| Concept | Description | Example |
|:--|:--|:--|
| **Data at Rest** | Stored data requiring encryption and access control. | Databases, backups |
| **Data in Transit** | Data moving across networks; protected via TLS/IPSec. | HTTPS traffic |
| **Data in Use** | Data actively processed in memory. | Active transaction processing |
| **Data Sovereignty** | Data governed by local legal frameworks. | EU GDPR compliance |
| **Geolocation** | Physical data storage location. | Cloud region selection |

---

### 🧰 Methods to Secure Data

| Method | Description | Example |
|:--|:--|:--|
| **Geographic Restrictions** | Limits access or services by region. | Geo-IP filtering |
| **Encryption** | Converts data into unreadable ciphertext. | AES-256, RSA |
| **Hashing** | Verifies data integrity with fixed-length output. | SHA-256 checksum |
| **Masking** | Conceals partial data for privacy. | Showing last 4 digits of SSN |
| **Tokenization** | Replaces sensitive values with placeholders. | Credit card tokenization |
| **Obfuscation** | Makes code or data difficult to interpret. | Variable name scrambling |
| **Segmentation** | Divides systems or networks to reduce risk. | VLAN or subnet isolation |
| **Permission Restrictions** | Limits data access to authorized roles. | RBAC, ACLs |

---

## 🧩 MCQ Sets

The `scenarios/` directory contains multiple-choice question sets covering this objective:

- **`set-01.json`** — Data types and classifications  
- **`set-02.json`** — Data states and security methods  

Each set includes:
- Four randomized answer choices  
- Real-world examples and explanations  
- Automatic shuffling for variety  

---

## 🧑‍💻 Lab Tasks

1. **Review the MCQ sets** under `scenarios/`.  
   Each question reinforces how to classify and protect data appropriately.  

2. **Run the quiz engine** (`lab.py`) to:  
   - Present randomized questions and choices  
   - Capture user input interactively  
   - Provide detailed feedback with examples  

3. **Hands on exercise**  
   - Compare how **data at rest** vs. **data in transit** are secured using encryption.  

---

### 🧠 Task: Compare Data-at-Rest vs. Data-in-Transit Encryption

#### 🎯 Objective
Demonstrate how encryption protects data in two different states:
- **At Rest** → stored on disk  
- **In Transit** → transmitted across a network

This exercise reinforces the concept that **data must be secured throughout its entire lifecycle**, not just during transmission.

---

## ✅ Acceptance Criteria

- MCQ sets fully cover Objective **3.3: Compare and contrast concepts and strategies to protect data**.  
- `lab.py` executes successfully with scoring and feedback.  
- Each question includes **examples** and **explanations**.  
- Optional demos illustrate encryption, hashing, or tokenization workflows.  

---

## ▶️ How to Run

**Python:**
```bash
cd lab-3-3-data-security-and-privacy/python
py lab.py
