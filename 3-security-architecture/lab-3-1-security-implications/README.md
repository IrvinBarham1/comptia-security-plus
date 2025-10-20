# Lab 3.1 — Security Architecture

## 🎯 Objective
**“Compare and contrast security implications of different architecture models.”**

This lab reinforces understanding of how infrastructure design decisions affect the **security, availability, and scalability** of enterprise environments—both on-premises and in the cloud.

---

## 📖 Background

Modern enterprise architecture combines **physical**, **virtual**, and **cloud-based** systems that must be securely integrated.  
Each model—whether centralized, distributed, or hybrid—presents unique security implications related to **data control**, **attack surface**, and **responsibility boundaries**.

Key architectural elements include:

| Concept | Description |
|:--|:--|
| **Cloud Responsibility Matrix** | Defines which security tasks are handled by the provider vs. the customer. |
| **Hybrid Cloud** | Combines on-premises and public cloud resources for flexibility and scalability. |
| **Infrastructure as Code (IaC)** | Uses code to automate the deployment of secure, consistent environments. |
| **Serverless / Microservices** | Reduces the attack surface but increases dependency complexity. |
| **Network Segmentation** | Limits lateral movement by isolating systems physically or logically. |
| **Software-Defined Networking (SDN)** | Centralizes control and enables programmable security policy enforcement. |
| **Containerization & Virtualization** | Provide isolation of workloads but require proper image and hypervisor security. |
| **IoT & Embedded Systems** | Expand attack surfaces; often lack strong patching or encryption support. |
| **ICS / SCADA & RTOS** | Operate in critical environments with strict uptime and real-time constraints. |
| **High Availability** | Ensures continuous operation through redundancy and fault tolerance. |

---

### 🔧 Architecture & Infrastructure Considerations

| Factor | Description |
|:--|:--|
| **Availability & Resilience** | Maintain uptime through redundancy, failover, and self-healing systems. |
| **Cost & Scalability** | Balance financial efficiency with the ability to grow or shrink resources dynamically. |
| **Ease of Deployment / Recovery** | Automation and documented processes simplify rollouts and restorations. |
| **Risk Transference** | Outsource or insure against potential losses (e.g., cloud providers, cyber-insurance). |
| **Patch Availability / Inability to Patch** | Evaluate vendor support lifecycles and legacy-system risk exposure. |
| **Power & Compute** | Ensure sufficient and redundant physical resources for reliability. |

---

## 🧩 MCQ Sets

Located under the `scenarios/` directory:

Each question includes:
- Four multiple-choice answers  
- Examples and concise explanations  
- Randomized question order on each run  

---

## 🧑‍💻 Lab Tasks

1. **Review the question sets** under `scenarios/`.  
   Each question tests your ability to identify design models and their security trade-offs.  

2. **Run the quiz engine** (`lab.py`) to:  
   - Present randomized questions and answer options  
   - Accept user input  
   - Score and display progress dynamically  

---

## ✅ Acceptance Criteria

- `set-01.json` and `set-02.json` together cover every concept in **Objective 3.1**  
- `lab.py` executes successfully and tracks scores with feedback  
- Each MCQ contains clear **examples** and **explanations**    

---

## ▶️ How to Run

**Python:**
```bash
cd lab-3-1-security-implications/python
py lab.py
