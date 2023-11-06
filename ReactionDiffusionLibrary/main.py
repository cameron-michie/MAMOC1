from pythonnet import load
import numpy as np
import matplotlib.pyplot as plt
from celluloid import Camera
from plotting import plot_imshow

load("coreclr")
import clr
clr.AddReference('/Users/cameronoscarmichie/Documents/GitHub/MAMOC/ReactionDiffusionLibrary/bin/Debug/net7.0/ReactionDiffusionLibrary.dll')
import ReactionDiffusionLibrary

with open("PopulationData.txt", 'w') as file:
    pass

gridxsize = 300
gridysize = 300

Prey_E0 = 200
Prey_N = 3000
Prey_EP = 30

Pred_E0 = 200
Pred_N = 3000
Pred_EP = 30

TheGrid = ReactionDiffusionLibrary.Grid(gridxsize, gridysize)
Prey = ReactionDiffusionLibrary.Species("Prey", Prey_E0, Prey_EP, Prey_N, TheGrid)
Pred = ReactionDiffusionLibrary.Species("Predator", Pred_E0, Pred_EP, Pred_N, TheGrid)

fig, ax = plt.subplots() 
cam = Camera(fig)
lastArr=[]

steps = 2000
for step in range(steps):
    Prey.Move()
    Pred.Move()
    TheGrid.Interact(Prey, Pred)
    fig, ax, lastArr = plot_imshow(fig, ax, lastArr)
    cam.snap()
    
TheGrid.SaveLineToFile(f"\nand all of that ^^^ was prey{Prey_EP} pred{Pred_EP}\n\n\n\n\n")
plt.close()
ani= cam.animate(interval = 30)
ani.save(f'Predator and prey simulation.mp4')
plt.close()