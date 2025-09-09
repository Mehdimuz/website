import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

# Time setup
T = 2*np.pi        # one full rotation
fps = 30
N = int(T*fps)
theta = np.linspace(0, T, N, endpoint=False)

# Unit circle coordinates
x_circle = np.cos(theta)
y_circle = np.sin(theta)

# Figure
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
fig.patch.set_facecolor("black")

def style_axes(ax):
    ax.set_facecolor("black")
    ax.tick_params(colors="white")
    for spine in ax.spines.values():
        spine.set_color("white")
    ax.xaxis.label.set_color("white")
    ax.yaxis.label.set_color("white")
    ax.title.set_color("white")
    ax.grid(True, color="gray", alpha=0.3)

# --- Left: unit circle ---
ax1.set_aspect('equal')
ax1.set_xlim(-1.2, 1.2)
ax1.set_ylim(-1.2, 1.2)
# ax1.set_title("Unit Circle: Geometry of Cos & Sin")
circle = plt.Circle((0,0), 1, fill=False, linestyle="--", color="gray", alpha=0.6)
ax1.add_patch(circle)

(point,) = ax1.plot([], [], 'o', color="red")
(line_radius,) = ax1.plot([], [], color="cyan", lw=2)
(line_cos,) = ax1.plot([], [], 'r--', lw=1.5)
(line_sin,) = ax1.plot([], [], 'g--', lw=1.5)

style_axes(ax1)
ax1.set_xlabel("Cos(θ)")
ax1.set_ylabel("Sin(θ)")

# --- Right: sine and cosine vs time ---
ax2.set_xlim(0, T)
ax2.set_ylim(-1.2, 1.2)
ax2.set_xlabel("Angle θ (radians)")
ax2.set_ylabel("Value")
(line_cos_t,) = ax2.plot([], [], color="green", lw=2, label="cos(θ)")
(line_sin_t,) = ax2.plot([], [], color="red", lw=2, label="sin(θ)")
(dot_cos,) = ax2.plot([], [], 'o', color="green")
(dot_sin,) = ax2.plot([], [], 'o', color="red")
ax2.legend(loc="upper right", facecolor="black", edgecolor="white", labelcolor="white")

style_axes(ax2)

def init():
    point.set_data([], [])
    line_radius.set_data([], [])
    line_cos.set_data([], [])
    line_sin.set_data([], [])
    line_cos_t.set_data([], [])
    line_sin_t.set_data([], [])
    dot_cos.set_data([], [])
    dot_sin.set_data([], [])
    return point, line_radius, line_cos, line_sin, line_cos_t, line_sin_t, dot_cos, dot_sin

def update(frame):
    th = theta[frame]
    x, y = np.cos(th), np.sin(th)

    # circle point + radius
    point.set_data([x], [y])
    line_radius.set_data([0, x], [0, y])

    # projection lines
    line_cos.set_data([0, x], [y, y])   # horizontal (cos)
    line_sin.set_data([x, x], [0, y])   # vertical (sin)

    # time waveforms
    line_cos_t.set_data(theta[:frame+1], np.cos(theta[:frame+1]))
    line_sin_t.set_data(theta[:frame+1], np.sin(theta[:frame+1]))
    dot_cos.set_data([th], [np.cos(th)])
    dot_sin.set_data([th], [np.sin(th)])

    return point, line_radius, line_cos, line_sin, line_cos_t, line_sin_t, dot_cos, dot_sin

ani = FuncAnimation(fig, update, frames=N, init_func=init, blit=True, interval=1000/fps)

gif_path = "unitcircle_dark.gif"
ani.save(gif_path, writer=PillowWriter(fps=fps), dpi=150)
print("Saved:", gif_path)
