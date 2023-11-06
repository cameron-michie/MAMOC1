import numpy as np
import matplotlib.pyplot as plt
from celluloid import Camera
from matplotlib.colors import ListedColormap

def lapalcian(X):
    return (np.roll(X, -1, axis=0) + np.roll(X, 1, axis=0) - 2 * X) / dx**2 + \
                  (np.roll(X, -1, axis=1) + np.roll(X, 1, axis=1) - 2 * X) / dx**2

def plot(ax):
    ax.matshow(X, cmap="Greens")
    reds = plt.cm.Reds(np.arange(256))
    reds[:, -1] = np.linspace(0, 1, 256)  # Make lower values more transparent.
    red_cmap = ListedColormap(reds)
    ax.imshow(Y, cmap=red_cmap, extent=[0, X.shape[1], 0, X.shape[0]])
    ax.set_xticks([])
    ax.set_yticks([])
    return ax

alpha, beta, gamma, delta = 0.1, 0.02, 0.3, 0.01
Dx, Dy = 0.1, 0.05  # Diffusion coefficients
dt = 0.01  # Time step
dx = 0.1  # Spatial step
L = 50  # Size of the grid
N = int(L / dx)

# Initialize populations
X = np.random.rand(N, N) * 40
Y = np.ones((N, N)) * 9
Y = np.random.rand(N, N) * 9
fig, ax = plt.subplots()
camera = Camera(fig)

steps = 2000
for t in range(steps):

    # Lotka-Volterras with diffusion laplacians
    laplacian_X, laplacian_Y = lapalcian(X), lapalcian(Y)
    dX = (alpha * X - beta * X * Y + Dx * laplacian_X) * dt
    dY = (-gamma * Y + delta * X * Y + Dy * laplacian_Y) * dt

    X += dX
    Y += dY

    ax = plot(ax)
    camera.snap()

animation = camera.animate(interval=5, blit=True)
animation.save('SpatialLotkaVolterra.mp4', writer='ffmpeg')

plt.show()