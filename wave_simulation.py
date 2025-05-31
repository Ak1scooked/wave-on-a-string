import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider, Button

# Basic string setup
L = 1.0
N = 200
x = np.linspace(0, L, N)
mu = 0.01
A0 = 0.1
wavelength = L / 2
k = 2 * np.pi / wavelength

# Initial parameters
T_init = 10.0
gamma_init = 1.0

def compute_wave_params(T):
    v = np.sqrt(T / mu)
    omega = v * k
    return v, omega

v, omega = compute_wave_params(T_init)

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.35)
line, = ax.plot(x, np.zeros_like(x), lw=2)
ax.set_ylim(-A0 * 1.2, A0 * 1.2)
ax.set_title("Interactive Wave on a String")
ax.set_xlabel("Position (m)")
ax.set_ylabel("Displacement (m)")

# Sliders
axcolor = 'lightgoldenrodyellow'
ax_tension = plt.axes([0.15, 0.22, 0.65, 0.03], facecolor=axcolor)
ax_damping = plt.axes([0.15, 0.17, 0.65, 0.03], facecolor=axcolor)
slider_tension = Slider(ax_tension, 'Tension (N)', 1, 100, valinit=T_init)
slider_damping = Slider(ax_damping, 'Damping γ', 0, 5, valinit=gamma_init)

# Button
ax_button = plt.axes([0.4, 0.05, 0.2, 0.05])
button = Button(ax_button, 'Toggle: Fixed Ends', color='lightblue', hovercolor='0.975')
state = {"boundary": "fixed"}

def toggle_boundary(event):
    if state["boundary"] == "fixed":
        state["boundary"] = "free"
        button.label.set_text("Toggle: Free Ends")
    else:
        state["boundary"] = "fixed"
        button.label.set_text("Toggle: Fixed Ends")

button.on_clicked(toggle_boundary)

# Update animation
def update(frame):
    T = slider_tension.val
    gamma = slider_damping.val
    v, omega = compute_wave_params(T)
    t = frame / 100

    y = A0 * np.exp(-gamma * t) * np.sin(k * x - omega * t)

    if state["boundary"] == "fixed":
        y[0] = 0
        y[-1] = 0
    elif state["boundary"] == "free":
        y[0] = y[1]
        y[-1] = y[-2]

    line.set_ydata(y)
    return line,

ani = FuncAnimation(fig, update, frames=np.arange(0, 1000), interval=20, blit=True)

plt.show()
