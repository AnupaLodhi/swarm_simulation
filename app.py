import streamlit as st
from swarm_simulation import Simulation

st.set_page_config(page_title="Swarm Simulation", layout="wide")
st.title("🤖 Adaptive Swarm-Based Task Allocation")
st.markdown("Decentralized multi-agent swarm simulation using ACO-inspired intelligence.")

if st.button("▶️ Run Simulation"):
    with st.spinner("Running simulation..."):
        sim = Simulation()
        sim.run()
    st.image("swarm_results.png", caption="Simulation Results")
