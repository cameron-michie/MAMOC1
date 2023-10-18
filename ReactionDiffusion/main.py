import numpy as np
from typing import Dict, List
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from celluloid import Camera
import time 
from funcs import *
from grid import Grid
from species import Species

gridxsize = 100
gridysize = 100

Prey_E0 = 200
Prey_EP = 10
Prey_N = 600

Pred_E0 = 200
Pred_EP = 10
Pred_N = 220
    
TheGrid = Grid(gridxsize, gridysize)
Prey = Species("Prey", Prey_E0, Prey_EP, Prey_N, TheGrid)
Pred = Species("Predator", Pred_E0, Pred_EP, Pred_N, TheGrid)
initialise_agents(Prey)
initialise_agents(Pred)

fig1, ax1 = plt.subplots()
cam1 = Camera(fig1)
fig2, ax2 = plt.subplots()
cam2 = Camera(fig2)

for i in range(1000):
    TheGrid.animals_in_grid = [[[] for _ in range(TheGrid.gridxsize)] for _ in range(TheGrid.gridysize)]

    Prey.move()
    Pred.move()
    interact(Prey, Pred, TheGrid)
    print(i, len(Prey.agents), len(Pred.agents))
    fig1, ax1 = plot_frame(fig1, ax1, Prey, Pred)
    cam1.snap()
    fig2, ax2 = plot_imshow(fig2, ax2, TheGrid)
    cam2.snap()
    

plt.close()
ani1= cam1.animate(interval = 35)
ani1.save('predatorprey.mp4')
ani2= cam2.animate(interval = 35)
ani2.save('predatorprey_imshow.mp4')
plt.close()