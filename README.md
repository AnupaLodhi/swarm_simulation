# 🤖 Adaptive Swarm-Based Cooperative Task Allocation
### Using Computational Intelligence (ACO-Inspired Multi-Agent Simulation)

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Live-FF4B4B?style=for-the-badge&logo=streamlit)
![NumPy](https://img.shields.io/badge/NumPy-Scientific-013243?style=for-the-badge&logo=numpy)
![Type](https://img.shields.io/badge/Type-AI%20Simulation-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge)

---

## 📌 Project Overview

This project implements a **decentralized, adaptive swarm intelligence system** for cooperative task allocation among multiple autonomous agents in a dynamic 2D simulated environment.

Inspired by **Ant Colony Optimization (ACO)**, agents independently evaluate and select tasks using pheromone trails, priority scores, and distance metrics — without any centralized controller.

The system also simulates **real-world challenges** like agent failure and energy depletion, demonstrating fault tolerance and adaptive reassignment.

> **Core Idea:** Multiple autonomous agents cooperate like a swarm of ants — no single leader, no central control — yet tasks get completed efficiently through collective intelligence.

---

## 🎯 Objectives

| Objective | Description |
|-----------|-------------|
| Decentralized Allocation | Agents select tasks independently using swarm logic |
| Adaptive Learning | Pheromone feedback adjusts future task selection |
| Fault Tolerance | System continues even when agents fail |
| Performance Evaluation | Metrics tracked across every simulation step |

---

## 🧠 How It Works

### ACO-Inspired Task Selection Formula

Each agent scores available tasks using:

```
Score = Pheromone^α × (Priority / Distance)^β
```

| Symbol | Meaning |
|--------|---------|
| α (Alpha) | Pheromone influence weight |
| β (Beta) | Heuristic (priority/distance) influence |
| Pheromone | Increases on success, evaporates over time |
| Priority | Task urgency level (1–5) |
| Distance | Euclidean distance from agent to task |

Tasks are then **probabilistically selected** — higher scores = higher chance of selection.

---

## ⚙️ System Architecture

```
┌─────────────────────────────────────────┐
│           SIMULATION ENGINE             │
│                                         │
│  ┌─────────────┐   ┌─────────────────┐  │
│  │ Task Module │   │  Agent Module   │  │
│  │  - Priority │   │  - Energy       │  │
│  │  - Location │   │  - Capability   │  │
│  │  - Effort   │   │  - Position     │  │
│  └──────┬──────┘   └────────┬────────┘  │
│         │                   │           │
│         ▼                   ▼           │
│  ┌─────────────────────────────────┐    │
│  │     Swarm Intelligence Module   │    │
│  │  - Pheromone Trails             │    │
│  │  - ACO Task Scoring             │    │
│  │  - Probabilistic Selection      │    │
│  └─────────────┬───────────────────┘    │
│                │                        │
│                ▼                        │
│  ┌─────────────────────────────────┐    │
│  │   Feedback & Adaptation Module  │    │
│  │  - Pheromone Deposit (success)  │    │
│  │  - Pheromone Evaporation        │    │
│  │  - Agent Failure Handling       │    │
│  └─────────────────────────────────┘    │
└─────────────────────────────────────────┘
```

---

## 📊 Simulation Results

> ▶️ Run the simulation first, then upload `swarm_results.png` to your GitHub repo to see the chart here.

![Simulation Results](swarm_results.png)

---

## 📊 Performance Metrics Tracked

| Metric | Description |
|--------|-------------|
| ✅ Task Completion Rate | % of tasks completed out of total |
| ⚡ Energy Consumption | Average agent energy per step |
| 🤖 Agent Survival Rate | Agents alive vs failed over time |
| ⏱️ Completion Time | Step at which each task was completed |
| 📈 Cumulative Progress | Tasks completed over simulation steps |

---

## 🛠️ Technology Stack

| Category | Tool |
|----------|------|
| Language | Python 3.8+ |
| Simulation | NumPy, Random |
| Visualization | Matplotlib |
| Web Interface | Streamlit |
| Algorithm | ACO (Ant Colony Optimization) |

---

## 📁 Project Structure

```
swarm_simulation/
│
├── swarm_simulation.py   # Core simulation engine
│                         # (Task, Agent, SwarmIntelligence, Simulation)
│
├── app.py                # Streamlit web interface
│
├── requirements.txt      # Python dependencies
│
├── swarm_results.png     # Auto-generated results chart
│
└── README.md             # Project documentation
```

---

## ▶️ How to Run Locally

**1. Clone the repository**
```bash
git clone https://github.com/AnupaLodhi/swarm_simulation.git
cd swarm_simulation
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run simulation directly**
```bash
python swarm_simulation.py
```

**4. Or run as Streamlit app**
```bash
streamlit run app.py
```

---

## 🌐 Live Demo

🔗 **[View Live App on Streamlit →](https://anupalodhi-swarm-simulation.streamlit.app)**

---

## 📈 Sample Output

```
=======================================================
  🤖 ADAPTIVE SWARM SIMULATION STARTING
=======================================================
  Agents: 6 | Tasks: 12 | Grid: 20x20
=======================================================
  ✅ Step 03 | Agent 2 completed Task 4 (priority=5)
  ✅ Step 05 | Agent 0 completed Task 7 (priority=3)
  ⚠️  Step 06 | Agent 4 FAILED!
  ✅ Step 08 | Agent 1 completed Task 2 (priority=4)
  🔋 Step 12 | Agent 3 ran out of energy!
  ...
  🎉 All tasks completed at step 38!
=======================================================
  📊 SIMULATION SUMMARY
=======================================================
  Total Steps Run     : 39
  Tasks Completed     : 12 / 12
  Completion Rate     : 100%
  Agents Alive        : 4 / 6
=======================================================
```

---

## 🔬 Key Concepts Demonstrated

- **Swarm Intelligence** — collective behavior without central control
- **Ant Colony Optimization (ACO)** — pheromone-based decision making
- **Multi-Agent Systems** — independent agents with shared environment
- **Fault Tolerance** — task reallocation on agent failure
- **Adaptive Learning** — pheromone feedback improves future decisions
- **Probabilistic Selection** — exploration vs exploitation balance

---

## 🚀 Future Enhancements

- Compare ACO vs PSO vs Genetic Algorithm performance
- Add obstacle avoidance in the 2D grid
- Implement real-time animated simulation
- Add hyperparameter tuning dashboard
- Deploy with agent count slider on Streamlit

---

## 👩‍💼 About This Project

This project was developed as part of an **academic major project** to demonstrate the application of Computational Intelligence in autonomous multi-agent systems.

**Skills demonstrated:**
- Swarm intelligence algorithm design
- Object-oriented Python programming
- Data visualization & simulation
- Performance analysis & metrics tracking

---

## 📬 Connect

 Anupa Lodhi
- 🔗 LinkedIn: (https://www.linkedin.com/in/anupalodhi12a/)
- 💻 GitHub: [github.com/AnupaLodhi](https://github.com/AnupaLodhi)

---

> *This project is developed for academic and portfolio purposes to demonstrate Computational Intelligence concepts.*
