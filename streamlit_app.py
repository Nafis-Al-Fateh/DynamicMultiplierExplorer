import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(page_title="Dynamic Multiplier Visualizer", layout="wide")

st.title("📊 Dynamic Multipliers in AR(1) Model")

st.markdown("""
This app visualizes how a shock propagates over time in an AR(1) model:

- Impact multiplier: β  
- Dynamic multipliers: ρ^k × β  
- Long-run multiplier: β / (1 - ρ)
""")

# Sidebar controls
st.sidebar.header("Parameters")

beta = st.sidebar.slider("Impact Multiplier (β)", -2.0, 2.0, 1.0, 0.1)
rho = st.sidebar.slider("Persistence (ρ)", -0.99, 0.99, 0.6, 0.01)
T = st.sidebar.slider("Number of Periods", 5, 50, 20)

# Compute dynamic multipliers
periods = np.arange(T)
dynamic_multipliers = beta * (rho ** periods)

# Long-run multiplier
if abs(rho) < 1:
    long_run = beta / (1 - rho)
else:
    long_run = np.nan

# Plot
fig, ax = plt.subplots(figsize=(10, 5))

# Bar plot (multipliers)
ax.bar(periods, dynamic_multipliers)

# Line plot (impulse response)
ax.plot(periods, dynamic_multipliers, marker='o')

# Long-run line
if not np.isnan(long_run):
    ax.axhline(long_run, linestyle='--')

ax.set_title("Dynamic Multiplier Path (Impulse Response)")
ax.set_xlabel("Time Period")
ax.set_ylabel("Effect on Output")

st.pyplot(fig)

# Display values
st.subheader("Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Impact Multiplier (β)", f"{beta:.2f}")
col2.metric("Persistence (ρ)", f"{rho:.2f}")
col3.metric("Long-run Multiplier", f"{long_run:.2f}" if not np.isnan(long_run) else "∞")

# Economic intuition
st.markdown("""
## 📖 Interpretation

- **β (Impact Multiplier):** Immediate jump in output  
- **ρ (Persistence):** Controls how long the effect lasts  
    - High ρ → slow decay  
    - Low ρ → fast decay  
- **Dynamic Multipliers:** Show adjustment path over time  
- **Long-run Multiplier:** Total cumulative effect  

### Key Insight:
- If ρ → 1 → very persistent shocks  
- If ρ < 0 → oscillating effects  
""")
