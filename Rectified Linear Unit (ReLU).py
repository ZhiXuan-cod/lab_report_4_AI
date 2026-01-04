import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="ReLU Activation", layout="centered")
st.title("ReLU Activation Function")
st.markdown("**Formula:** f(x) = max(0, x)")

x = np.linspace(-10, 10, 500)
y = np.maximum(0, x)

fig, ax = plt.subplots()
ax.plot(x, y, color='blue', linewidth=2)
ax.grid(True)
ax.set_xlabel("Input")
ax.set_ylabel("Output")
ax.set_title("ReLU Activation")
st.pyplot(fig)

st.markdown("### Characteristics:")
st.write("- Output: 0 for negative inputs, linear for positive inputs")
st.write("- Avoids vanishing gradient problem")
st.write("- Computationally efficient")
st.write("- Commonly used in hidden layers")

st.markdown("---")
st.write("**GitHub:** https://github.com/yourusername/bsd3513-lab5")
st.write("**Live App:** https://relu-activation.streamlit.app")