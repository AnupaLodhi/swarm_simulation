import streamlit as st
import matplotlib
matplotlib.use('Agg')
import os
from swarm_simulation import Simulation

st.set_page_config(page_title="Swarm Simulation", layout="wide")

st.title("🤖 Adaptive Swarm-Based Task Allocation")
st.markdown("Decentralized multi-agent swarm simulation using ACO-inspired intelligence.")

st.info("👆 Click the button below to run the simulation and generate results.")

if st.button("▶️ Run Simulation"):
    with st.spinner("⏳ Running simulation... please wait"):
        sim = Simulation()
        sim.run()
    st.success("✅ Simulation Complete!")

    # Show image only after simulation runs
    if os.path.exists("swarm_results.png"):
        st.subheader("📊 Simulation Results")
        st.image("swarm_results.png", caption="Swarm Simulation Results", use_column_width=True)
    else:
        st.warning("⚠️ Chart not generated. Please try running again.")

    # Show summary metrics
    st.subheader("📈 Performance Summary")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Tasks", sim.total_completed)
    col2.metric("Total Steps", sim.step + 1)
    alive = sum(1 for a in sim.agents if a.alive)
    col3.metric("Agents Alive", f"{alive} / {len(sim.agents)}")
