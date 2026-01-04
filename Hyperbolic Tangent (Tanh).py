import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Tanh Activation", layout="centered")
st.title("Tanh Activation Function")
st.markdown("**Formula:** f(x) = (e^x - e^(-x)) / (e^x + e^(-x))")

x = np.linspace(-10, 10, 500)
y = np.tanh(x)

fig, ax = plt.subplots()
ax.plot(x, y, color='red', linewidth=2)
ax.grid(True)
ax.set_xlabel("Input")
ax.set_ylabel("Output")
ax.set_title("Tanh Activation")
st.pyplot(fig)

st.markdown("### Characteristics:")
st.write("- Output range: (-1, 1)")
st.write("- Zero-centered output")
st.write("- Better gradient flow than sigmoid")
st.write("- Commonly used in RNNs")

st.markdown("---")
st.write("**GitHub:** https://github.com/yourusername/bsd3513-lab5")
st.write("**Live App:** https://tanh-activation.streamlit.app")