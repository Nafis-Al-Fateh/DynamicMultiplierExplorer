import numpy as np
import matplotlib
matplotlib.use("Agg")  # Safe backend for Streamlit Cloud
import matplotlib.pyplot as plt
import streamlit as st

# Page config
st.set_page_config(page_title="Dynamic Multiplier Explorer", layout="wide")

# Title
st.title("📊 Dynamic Multiplier Explorer")

st.markdown("""
Visualize how a shock propagates in an AR(1) model:

- **Impact multiplier (β)** → immediate effect  
- **Dynamic multipliers (ρ^k β)** → persistence over time  
- **Long-run multiplier (β / (1 − ρ))** → total cumulative effect  
""")

# Sidebar controls
st.sidebar.header("⚙️ Parameters")

beta = st.sidebar.slider("Impact Multiplier (β)", -2.0, 2.0, 1.0, 0.1)
rho = st.sidebar.slider("Persistence (ρ)", -0.99, 0.99, 0.6, 0.01)
T = st.sidebar.slider("Number of Periods (T)", 5, 50, 20)

# Compute values
periods = np.arange(T)
dynamic_multipliers = beta * (rho ** periods)

# Long-run multiplier
if abs(rho) < 1:
    long_run = beta / (1 - rho)
else:
    long_run = np.nan

# Layout
col1, col2 = st.columns([1, 2])

# Metrics (left side)
with col1:
    st.subheader("📌 Key Metrics")
    st.metric("Impact Multiplier (β)", f"{beta:.2f}")
    st.metric("Persistence (ρ)", f"{rho:.2f}")
    st.metric(
        "Long-run Multiplier",
        f"{long_run:.2f}" if not np.isnan(long_run) else "∞"
    )

# Plot (right side)
with col2:
    fig, ax = plt.subplots(figsize=(6, 3))  # smaller, compact

    # Bars
    ax.bar(periods, dynamic_multipliers)

    # Line (impulse response)
    ax.plot(periods, dynamic_multipliers, marker='o')

    # Long-run line
    if not np.isnan(long_run):
        ax.axhline(long_run, linestyle='--')

    ax.set_title("Dynamic Multiplier Path")
    ax.set_xlabel("Time")
    ax.set_ylabel("Effect on Output")

    st.pyplot(fig, use_container_width=True)

# Interpretation
st.markdown("""
## 📖 Interpretation

- **β (Impact Multiplier):** Immediate jump in output  
- **ρ (Persistence):**
  - Higher → slower decay (long-lasting shocks)  
  - Lower → faster decay  
  - Negative → oscillating pattern  

- **Dynamic Multipliers:** Show how the shock evolves over time  
- **Long-run Multiplier:** Total accumulated effect  

### 🔍 Key Insight:
- When **ρ → 1**, shocks persist for a long time  
- When **ρ is small**, system stabilizes quickly  
""")
