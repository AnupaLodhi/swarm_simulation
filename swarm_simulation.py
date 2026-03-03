"""
Adaptive Swarm-Based Cooperative Task Allocation
Using Computational Intelligence (ACO-inspired)

Author: Anupa Lodhi
Description: Multi-agent swarm simulation with decentralized
             task allocation, adaptive learning, and fault tolerance.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import random
import time

# ─────────────────────────────────────────────
# CONFIGURATION
# ─────────────────────────────────────────────
GRID_SIZE     = 20       # 2D grid dimensions
NUM_AGENTS    = 6        # number of agents
NUM_TASKS     = 12       # number of tasks
MAX_ENERGY    = 100      # max agent energy
FAILURE_PROB  = 0.05     # probability of agent failure per step
MAX_STEPS     = 50       # max simulation steps
ALPHA         = 1.0      # pheromone influence
BETA          = 2.0      # distance influence
EVAPORATION   = 0.1      # pheromone evaporation rate
random.seed(42)
np.random.seed(42)


# ─────────────────────────────────────────────
# TASK CLASS
# ─────────────────────────────────────────────
class Task:
    def __init__(self, tid):
        self.id       = tid
        self.x        = random.randint(0, GRID_SIZE - 1)
        self.y        = random.randint(0, GRID_SIZE - 1)
        self.priority = random.randint(1, 5)       # 1=low, 5=high
        self.effort   = random.randint(5, 20)      # energy required
        self.done     = False
        self.assigned = False

    def __repr__(self):
        return f"Task({self.id}, pri={self.priority}, pos=({self.x},{self.y}))"


# ─────────────────────────────────────────────
# AGENT CLASS
# ─────────────────────────────────────────────
class Agent:
    def __init__(self, aid):
        self.id         = aid
        self.x          = random.randint(0, GRID_SIZE - 1)
        self.y          = random.randint(0, GRID_SIZE - 1)
        self.energy     = random.randint(60, MAX_ENERGY)
        self.alive      = True
        self.task       = None       # currently assigned task
        self.completed  = 0          # tasks completed
        self.capability = random.uniform(0.6, 1.0)  # efficiency factor

    def distance_to(self, task):
        return np.sqrt((self.x - task.x)**2 + (self.y - task.y)**2)

    def move_toward(self, task):
        """Move one step toward task location."""
        if self.x < task.x: self.x += 1
        elif self.x > task.x: self.x -= 1
        if self.y < task.y: self.y += 1
        elif self.y > task.y: self.y -= 1

    def __repr__(self):
        return f"Agent({self.id}, energy={self.energy:.1f}, alive={self.alive})"


# ─────────────────────────────────────────────
# SWARM INTELLIGENCE MODULE
# ─────────────────────────────────────────────
class SwarmIntelligence:
    def __init__(self, tasks):
        self.pheromones = {t.id: 1.0 for t in tasks}  # initial pheromone

    def evaporate(self):
        """Evaporate pheromones each step."""
        for tid in self.pheromones:
            self.pheromones[tid] *= (1 - EVAPORATION)
            self.pheromones[tid] = max(0.1, self.pheromones[tid])

    def deposit(self, task, success):
        """Deposit pheromone based on task outcome."""
        reward = task.priority * (1.5 if success else 0.3)
        self.pheromones[task.id] += reward

    def select_task(self, agent, tasks):
        """
        ACO-inspired probabilistic task selection.
        Score = pheromone^alpha * (priority / distance)^beta
        """
        available = [t for t in tasks if not t.done and not t.assigned]
        if not available:
            return None

        scores = []
        for t in available:
            dist = max(agent.distance_to(t), 0.1)
            pher = self.pheromones[t.id] ** ALPHA
            heur = (t.priority / dist) ** BETA
            scores.append(pher * heur)

        total = sum(scores)
        probs = [s / total for s in scores]

        # Probabilistic selection
        chosen = np.random.choice(available, p=probs)
        return chosen


# ─────────────────────────────────────────────
# SIMULATION ENGINE
# ─────────────────────────────────────────────
class Simulation:
    def __init__(self):
        self.tasks   = [Task(i) for i in range(NUM_TASKS)]
        self.agents  = [Agent(i) for i in range(NUM_AGENTS)]
        self.swarm   = SwarmIntelligence(self.tasks)
        self.step    = 0

        # Metrics tracking
        self.metrics = {
            'completed_per_step': [],
            'energy_per_step':    [],
            'alive_per_step':     [],
            'completion_times':   [],
        }
        self.total_completed = 0
        self.start_time = time.time()

    def run(self):
        print("=" * 55)
        print("  🤖 ADAPTIVE SWARM SIMULATION STARTING")
        print("=" * 55)
        print(f"  Agents: {NUM_AGENTS} | Tasks: {NUM_TASKS} | Grid: {GRID_SIZE}x{GRID_SIZE}")
        print("=" * 55)

        for step in range(MAX_STEPS):
            self.step = step
            completed_this_step = 0
            total_energy = 0

            # Evaporate pheromones
            self.swarm.evaporate()

            for agent in self.agents:
                if not agent.alive:
                    continue

                # Random agent failure
                if random.random() < FAILURE_PROB:
                    agent.alive = False
                    if agent.task:
                        agent.task.assigned = False
                        agent.task = None
                    print(f"  ⚠️  Step {step:02d} | Agent {agent.id} FAILED!")
                    continue

                # Assign task if none
                if agent.task is None:
                    agent.task = self.swarm.select_task(agent, self.tasks)
                    if agent.task:
                        agent.task.assigned = True

                # Execute task
                if agent.task:
                    agent.move_toward(agent.task)
                    energy_cost = agent.task.effort * (1 / agent.capability) * 0.1
                    agent.energy -= energy_cost

                    # Check if reached task
                    if agent.x == agent.task.x and agent.y == agent.task.y:
                        if agent.energy >= agent.task.effort * 0.1:
                            # Task completed
                            agent.task.done = True
                            self.swarm.deposit(agent.task, success=True)
                            agent.completed += 1
                            completed_this_step += 1
                            self.total_completed += 1
                            self.metrics['completion_times'].append(step)
                            print(f"  ✅ Step {step:02d} | Agent {agent.id} completed Task {agent.task.id} (priority={agent.task.priority})")
                            agent.task = None
                        else:
                            # Not enough energy
                            self.swarm.deposit(agent.task, success=False)
                            agent.task.assigned = False
                            agent.task = None

                    # Energy depletion
                    if agent.energy <= 0:
                        agent.alive = False
                        if agent.task:
                            agent.task.assigned = False
                            agent.task = None
                        print(f"  🔋 Step {step:02d} | Agent {agent.id} ran out of energy!")

                total_energy += max(agent.energy, 0)

            # Record metrics
            alive_count = sum(1 for a in self.agents if a.alive)
            self.metrics['completed_per_step'].append(completed_this_step)
            self.metrics['energy_per_step'].append(total_energy / max(alive_count, 1))
            self.metrics['alive_per_step'].append(alive_count)

            # Stop if all tasks done
            if all(t.done for t in self.tasks):
                print(f"\n  🎉 All tasks completed at step {step}!")
                break

        self.print_summary()
        self.visualize()

    def print_summary(self):
        elapsed = time.time() - self.start_time
        print("\n" + "=" * 55)
        print("  📊 SIMULATION SUMMARY")
        print("=" * 55)
        print(f"  Total Steps Run     : {self.step + 1}")
        print(f"  Tasks Completed     : {self.total_completed} / {NUM_TASKS}")
        print(f"  Completion Rate     : {self.total_completed/NUM_TASKS*100:.1f}%")
        alive = sum(1 for a in self.agents if a.alive)
        print(f"  Agents Alive        : {alive} / {NUM_AGENTS}")
        print(f"  Simulation Time     : {elapsed:.2f}s")
        print("\n  Agent Performance:")
        for a in self.agents:
            status = "✅ Alive" if a.alive else "❌ Failed"
            print(f"    Agent {a.id}: {a.completed} tasks | Energy: {max(a.energy,0):.1f} | {status}")
        print("=" * 55)

    def visualize(self):
        fig, axes = plt.subplots(2, 2, figsize=(14, 10))
        fig.suptitle("🤖 Adaptive Swarm Simulation Results", fontsize=16, fontweight='bold')
        fig.patch.set_facecolor('#0f0f0f')
        for ax in axes.flat:
            ax.set_facecolor('#1a1a1a')
            ax.tick_params(colors='white')
            ax.xaxis.label.set_color('white')
            ax.yaxis.label.set_color('white')
            ax.title.set_color('white')
            for spine in ax.spines.values():
                spine.set_edgecolor('#444')

        steps = range(len(self.metrics['completed_per_step']))

        # ── Plot 1: Tasks completed per step
        ax1 = axes[0, 0]
        cumulative = np.cumsum(self.metrics['completed_per_step'])
        ax1.plot(steps, cumulative, color='#FFD700', linewidth=2.5, marker='o', markersize=3)
        ax1.fill_between(steps, cumulative, alpha=0.2, color='#FFD700')
        ax1.set_title("Cumulative Task Completion")
        ax1.set_xlabel("Step")
        ax1.set_ylabel("Tasks Completed")
        ax1.axhline(NUM_TASKS, color='#FF6B6B', linestyle='--', alpha=0.6, label='Total Tasks')
        ax1.legend(facecolor='#2a2a2a', labelcolor='white')

        # ── Plot 2: Average energy per step
        ax2 = axes[0, 1]
        ax2.plot(steps, self.metrics['energy_per_step'], color='#00E5FF', linewidth=2)
        ax2.fill_between(steps, self.metrics['energy_per_step'], alpha=0.15, color='#00E5FF')
        ax2.set_title("Avg Agent Energy Over Time")
        ax2.set_xlabel("Step")
        ax2.set_ylabel("Energy")

        # ── Plot 3: Alive agents per step
        ax3 = axes[1, 0]
        ax3.step(steps, self.metrics['alive_per_step'], color='#69FF47', linewidth=2, where='mid')
        ax3.fill_between(steps, self.metrics['alive_per_step'], alpha=0.15, color='#69FF47', step='mid')
        ax3.set_title("Active Agents Over Time")
        ax3.set_xlabel("Step")
        ax3.set_ylabel("Alive Agents")
        ax3.set_ylim(0, NUM_AGENTS + 1)

        # ── Plot 4: Final grid map
        ax4 = axes[1, 1]
        ax4.set_xlim(0, GRID_SIZE)
        ax4.set_ylim(0, GRID_SIZE)
        ax4.set_title("Final Agent & Task Map")
        ax4.set_xlabel("X")
        ax4.set_ylabel("Y")
        ax4.grid(True, alpha=0.15, color='white')

        for t in self.tasks:
            color = '#555' if t.done else '#FFD700'
            marker = 'x' if t.done else '*'
            ax4.scatter(t.x, t.y, c=color, s=120, marker=marker, zorder=3)
            ax4.annotate(f"T{t.id}", (t.x, t.y), textcoords="offset points",
                         xytext=(4, 4), fontsize=7, color=color)

        for a in self.agents:
            color = '#00E5FF' if a.alive else '#FF4444'
            ax4.scatter(a.x, a.y, c=color, s=180, marker='^', zorder=4, edgecolors='white', linewidths=0.5)
            ax4.annotate(f"A{a.id}", (a.x, a.y), textcoords="offset points",
                         xytext=(4, -10), fontsize=7, color=color)

        legend_elements = [
            mpatches.Patch(color='#FFD700', label='Pending Task'),
            mpatches.Patch(color='#555555', label='Completed Task'),
            mpatches.Patch(color='#00E5FF', label='Active Agent'),
            mpatches.Patch(color='#FF4444', label='Failed Agent'),
        ]
        ax4.legend(handles=legend_elements, facecolor='#2a2a2a', labelcolor='white', fontsize=8)

        plt.tight_layout()
        plt.savefig("swarm_results.png", dpi=150, bbox_inches='tight', facecolor='#0f0f0f')
        plt.show()
        print("\n  📸 Chart saved as swarm_results.png")


# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────
if __name__ == "__main__":
    sim = Simulation()
    sim.run()