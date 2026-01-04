import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Tanh Visualizer", layout="centered")
st.title("Tanh Activation Function")

# User controls
n_points = st.slider("Number of values in graph:", 50, 1000, 500, 50)
x_range = st.slider("X-axis range:", -10.0, 10.0, (-5.0, 5.0), 0.5)

# Generate data
x = np.linspace(x_range[0], x_range[1], n_points)
y = np.tanh(x)

# Plot
fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(x, y, linewidth=2, color='green')
ax.axhline(0, color='gray', linewidth=0.5)
ax.axvline(0, color='gray', linewidth=0.5)
ax.grid(True, alpha=0.3)
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.set_title(f'Tanh: f(x) = tanh(x) | Points: {n_points}')
st.pyplot(fig)