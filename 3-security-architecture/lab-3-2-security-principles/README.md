# Lab 3.2 — Security Architecture

## 🎯 Objective
**“Given a scenario, apply security principles to secure enterprise infrastructure.”**

This lab focuses on designing and applying **defense-in-depth strategies** within enterprise networks.  
You’ll explore how infrastructure components, secure communication methods, and layered controls work together to harden systems and minimize attack surfaces.

---

## 📖 Background

Securing enterprise infrastructure requires both **proper architecture** and **control enforcement** across every network layer.  
Organizations must strategically place devices, select appropriate security zones, and maintain secure communication channels to reduce exposure and improve visibility.

### Infrastructure Security Concepts

| Concept | Description |
|:--|:--|
| **Device Placement** | Positioning of security tools such as firewalls, proxies, and IDS/IPS sensors for maximum protection. |
| **Security Zones** | Logical or physical network boundaries separating different trust levels (e.g., internal, DMZ, guest). |
| **Attack Surface** | All possible entry points where an attacker could exploit vulnerabilities. |
| **Connectivity** | Secure communication paths that support redundancy and encrypted traffic. |
| **Failure Modes** | Determines whether a system blocks (fail-closed) or allows (fail-open) traffic during failure. |
| **Device Attributes** | Defines how devices interact with traffic (active vs. passive, inline vs. tap). |
| **Network Appliances** | Security tools such as jump servers, proxies, IDS/IPS, load balancers, and sensors. |
| **Port Security** | Controls device authentication on switch ports using 802.1X and EAP. |
| **Firewall Types** | Includes WAF, UTM, and NGFW solutions operating at different OSI layers. |

---

### Secure Communication and Access

| Technology | Description |
|:--|:--|
| **Virtual Private Network (VPN)** | Creates encrypted tunnels over untrusted networks for remote or site-to-site access. |
| **Remote Access** | Enables secure user connectivity with authentication and encryption. |
| **Tunneling** | Encapsulates packets within secure protocols to hide internal traffic. |
| **Transport Layer Security (TLS)** | Provides encryption for web and application-layer traffic. |
| **Internet Protocol Security (IPSec)** | Encrypts and authenticates IP packets for secure network-level communication. |
| **Software-Defined Wide Area Network (SD-WAN)** | Centrally manages and routes WAN traffic for security and performance. |
| **Secure Access Service Edge (SASE)** | Cloud-based model combining SD-WAN and security services into one architecture. |
| **Selection of Effective Controls** | Choosing appropriate technical and administrative safeguards based on risk tolerance. |

---

## 🧩 MCQ Sets

The `scenarios/` folder contains multiple-choice question sets for this objective:

Each set includes:
- Four randomized answer choices  
- Examples and detailed explanations  
- Automatic shuffling of questions at runtime  

---

## 🧑‍💻 Lab Tasks

1. **Review the question sets** under `scenarios/`.  
   Each item tests your ability to identify appropriate architecture controls or secure communication methods.

2. **Run the quiz engine** (`lab.py`) to:  
   - Present randomized questions and answer options  
   - Capture user input interactively  
   - Track your cumulative score with feedback  

3. **Hands on exercise**  
   - Configure a simulated **DMZ** with an inline firewall and monitoring sensor.  
---

## 🧱 DMZ Simulation Lab — Inline Firewall and Monitoring Sensor

The **Demilitarized Zone (DMZ)** isolates publicly accessible services (like web or mail servers) from the internal network to limit exposure.

### 🧰 Objective
Simulate a basic DMZ using virtual networking and demonstrate:
- Inline traffic filtering by a **firewall**
- Passive monitoring by an **IDS sensor**

### ⚙️ Setup Steps
1. **Create Virtual Networks**  
   - `dmz_net` → hosts web server (e.g., `192.168.10.0/24`)  
   - `internal_net` → hosts private systems (e.g., `192.168.20.0/24`)  

2. **Configure the Inline Firewall**
   ```bash
   sudo iptables -A FORWARD -i dmz_net -o internal_net -m state --state ESTABLISHED,RELATED -j ACCEPT
   sudo iptables -A FORWARD -i internal_net -o dmz_net -p tcp --dport 443 -j ACCEPT
   sudo iptables -A FORWARD -j DROP

---

## ✅ Acceptance Criteria

- MCQ sets comprehensively cover **Objective 3.2** (infrastructure and secure access).  
- `lab.py` executes successfully and provides scoring with real-time feedback.  
- Each question includes **examples** and **explanations** for reinforcement.  
- Optional demos demonstrate understanding of segmentation, secure tunnels, and layered defenses.  

---

## ▶️ How to Run

**Python:**
```bash
cd lab-3-2-security-principles/python
py lab.py