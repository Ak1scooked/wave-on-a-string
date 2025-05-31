import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Wave on a String")

T = st.slider("Tension", 1.0, 100.0, 10.0)
gamma = st.slider("Damping", 0.0, 5.0, 1.0)
L = 1.0
N = 200
x = np.linspace(0, L, N)
k = 2 * np.pi / (L / 2)
mu = 0.01
v = np.sqrt(T / mu)
omega = v * k
t = st.slider("Time", 0.0, 2.0, 0.0, 0.01)
A0 = 0.1

y = A0 * np.exp(-gamma * t) * np.sin(k * x - omega * t)

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_ylim(-0.2, 0.2)
st.pyplot(fig)
