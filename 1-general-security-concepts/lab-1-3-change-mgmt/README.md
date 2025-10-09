# Lab 1.3 — Change & Configuration Management

## 🎯 Objective

**“Explain the importance of change and configuration management concepts.”**

Practice recognizing and applying **business processes, technical implications, and documentation practices** related to secure change management.

---

## 📖 Background

Change and configuration management ensures that modifications to IT systems are properly **planned, documented, approved, and tested** to minimize risk and disruption.

### Business Processes Impacting Security Operations
- **Approval process** — formal review of requested changes  
- **Ownership** — identifies the individual or team initiating the change  
- **Stakeholders** — parties impacted or invested in the change  
- **Impact analysis** — evaluates potential disruptions or benefits  
- **Test results** — confirm changes work as intended  
- **Backout plan** — rollback procedure if something fails  
- **Maintenance window** — designated timeframe for changes  
- **Standard operating procedure (SOP)** — consistent step-by-step process  

### Technical Implications of Changes
- **Allow lists / Deny lists** — define permitted or blocked entities  
- **Restricted activities** — prohibit tasks that pose risks  
- **Downtime** — all changes carry outage risk  
- **Service restart** — some patches require services to restart  
- **Application restart** — client apps may need restarting after updates  
- **Legacy applications** — older systems sensitive to changes  
- **Dependencies** — interconnected systems that can cascade failures  

### Documentation
- **Documenting changes** — provides accountability and historical record  
- **Version control** — manages changes to files and configurations  
- **Proper documentation** — updating diagrams, policies, and tickets  
- **Continuous improvement** — refining the process after each change  
- **Records** — requests and tickets provide clear timelines  

---

## 🧑‍💻 Lab Tasks

1. **Review the questions** in the `scenarios/` folder (e.g., `set-01.json`).  
   Each question maps to a concept under Objective 1.3.  

2. **Answer each question** in multiple-choice format.  
   - Questions are shuffled on each run for variety  
   - Feedback includes **examples** and **explanations**  

3. **Run the quiz engine** (`lab.py`) to:  
   - Present questions and answer choices  
   - Accept user input  
   - Score and display progress  

---

## ✅ Acceptance Criteria

- MCQs in `set-01.json` and  `set-02.json` covering every bullet of Objective 1.3  
- `lab.py` runs successfully and provides scoring with feedback  
- Each question includes **examples** and an **explanation** for reinforcement  

---

## ▶️ How to Run

**Python:**  
```bash
cd lab-1-3-change-mgmt\python

# Run the multiple-choice quiz
py lab.py
```

---

## 📝 Reflection

This lab reinforced how business processes, technical implications, and documentation are intertwined in change management. Practicing these scenarios helped connect terminology (CAB, backout plans, dependencies) to real-world IT operations.