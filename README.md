# 🐜 Swarm Intelligence — PSO-Based Multi-Agent Simulation

> A fully interactive, browser-based simulation of Swarm Intelligence using a Particle Swarm Optimization (PSO)-inspired algorithm on a 2D grid. Built with pure HTML, CSS, and JavaScript — no libraries, no frameworks.

![Swarm Intelligence Demo](https://img.shields.io/badge/Demo-Live-brightgreen) ![Language](https://img.shields.io/badge/Language-HTML%20%2F%20JS-orange) ![Algorithm](https://img.shields.io/badge/Algorithm-PSO-blue) ![License](https://img.shields.io/badge/License-MIT-lightgrey)



Live Demo

[View Live Site](https://anupalodhi.github.io/swarm_intelligent/)]


## 📌 What Is Swarm Intelligence?

Swarm Intelligence is a field of AI where a group of **simple, autonomous agents** — each following basic local rules — collectively produce **complex, intelligent behavior** without any central controller.

> Think of it like an ant colony. Each ant is "dumb" — it only knows what's directly around it. But together, 500,000 ants can build cities, farm food, and solve the shortest-path problem. That's swarm intelligence.

---

## 🧠 Algorithm Used — PSO (Particle Swarm Optimization)

Each agent updates its velocity every iteration using three forces:

```
v(t+1) = ω · v(t) + c₁ · r₁ · (pBest - x) + c₂ · r₂ · (target - x)
```

| Symbol | Meaning |
|--------|---------|
| `ω` | Inertia weight — keeps agent moving in current direction |
| `c₁` | Cognitive coefficient — pulls toward agent's personal best |
| `c₂` | Social coefficient — pulls toward nearest task |
| `r₁, r₂` | Random values (0 to 1) for stochasticity |
| `pBest` | Agent's personal best position so far |
| `target` | Nearest live task on the grid |

---

## 🗂️ Project Structure

```
swarm-intelligence/
│
├── index.html       ← Complete simulation + web page (single file)
└── README.md        ← This file
```

---

## ⚙️ Simulation Parameters

| Parameter | Default | Range | Description |
|-----------|---------|-------|-------------|
| Grid Size | 52 × 30 | Fixed | 2D environment space |
| Agents | 15 | 3 – 30 | Number of autonomous agents |
| Tasks | 10 | 3 – 20 | Number of target objectives |
| Inertia (ω) | 0.5 | — | Velocity carry-over weight |
| Cognitive (c₁) | 1.5 | — | Personal best attraction |
| Social (c₂) | 1.8 | — | Target attraction strength |
| Max Speed | 2.8 | — | Velocity clamp per iteration |

All parameters except grid size are adjustable live in the browser.

---

## 🔄 How It Works — Step by Step

```
1. Initialize agents randomly on the 2D grid
2. Place task nodes at random positions
3. For each iteration:
   a. Each agent finds its nearest alive task
   b. Updates velocity using PSO formula
   c. Clamps speed to max limit
   d. Moves to new position
   e. Checks if close enough to complete a task
4. Repeat until all tasks are completed
5. Log completion events and display metrics
```

---

## 🌍 Real-World Applications

| Domain | Application | Outcome |
|--------|------------|---------|
| 🚁 Drones | Search & Rescue after disasters | Parallel area coverage, no central coordinator |
| 📦 Logistics | Amazon Kiva warehouse robots | 4× faster order processing |
| 🚦 Traffic | Smart city traffic light control | 25% less travel time |
| 🔬 Medicine | Nanobot drug delivery swarms | Targeted tumor treatment |
| 🌐 Networks | Internet packet routing | Self-healing, millisecond rerouting |
| 📈 Finance | Quantitative trading optimization | Parallel parameter space exploration |

---

## ✅ Key Properties Demonstrated

- **Decentralization** — No central controller; each agent decides independently
- **Self-Organization** — Order emerges from local interactions
- **Fault Tolerance** — Removing agents doesn't break the system
- **Scalability** — Add more agents without changing the algorithm
- **Collective Intelligence** — Group solves what individuals cannot

---

## 🚀 How to Run

### Option 1 — Run locally
```bash
# Clone the repository
git clone https://github.com/yourusername/swarm-intelligence.git

# Open in browser
open index.html
```

### Option 2 — View on GitHub Pages
Just visit the live link above — no installation needed.

---

## 🛠️ Built With

- **Pure HTML5** — Structure and layout
- **Vanilla JavaScript** — PSO simulation engine
- **HTML5 Canvas** — Real-time 2D rendering
- **CSS3** — Animations and responsive design
- **Google Fonts** — Syne + DM Sans typography

No npm. No build step. No dependencies. Just open and run.

---

## 📊 Performance Metrics

| Metric | Description |
|--------|-------------|
| Task Completion Time | Iterations needed to complete all tasks |
| Scalability | Linear — works with 3 to 30+ agents |
| Fault Tolerance | No single point of failure |
| Convergence | Agents self-organize within first 50 iterations typically |

---

## 🔬 Possible Extensions

- [ ] Add **Ant Colony Optimization (ACO)** with pheromone trails
- [ ] Implement **Boids flocking** behavior (separation, alignment, cohesion)
- [ ] Add **obstacles** on the grid for path-finding scenarios
- [ ] PSO vs ACO **side-by-side comparison**
- [ ] Export simulation data as **CSV for analysis**
- [ ] Add **adaptive learning** — agents improve inertia over time

---

## 👨‍💻 Author

Anupa Lodhi
B.Tech CSE — Artificial Intelligence  
[GitHub](https://github.com/AnupaLodhi) · [LinkedIn](https://linkedin.com/in/anupalodhi12a/)

---

## 📄 License

This project is licensed under the **MIT License** — free to use, modify, and distribute.

---

> *"None of us is as smart as all of us."* — Kenneth Blanchard  
 developed for academic and portfolio purposes to demonstrate Computational Intelligence concepts.*
