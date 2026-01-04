import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Sigmoid Activation", layout="centered")
st.title("Sigmoid Activation Function")
st.markdown("**Formula:** f(x) = 1 / (1 + e^(-x))")

x = np.linspace(-10, 10, 500)
y = 1 / (1 + np.exp(-x))

fig, ax = plt.subplots()
ax.plot(x, y, color='green', linewidth=2)
ax.grid(True)
ax.set_xlabel("Input")
ax.set_ylabel("Output")
ax.set_title("Sigmoid Activation")
st.pyplot(fig)

st.markdown("### Characteristics:")
st.write("- Output range: (0, 1)")
st.write("- Smooth gradient")
st.write("- Used for binary classification output")
st.write("- Prone to vanishing gradients")

st.markdown("---")
st.write("**GitHub:** https://github.com/yourusername/bsd3513-lab5")
st.write("**Live App:** https://sigmoid-activation.streamlit.app")