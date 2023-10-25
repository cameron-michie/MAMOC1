from pythonnet import load
import numpy as np
import matplotlib.pyplot as plt
from celluloid import Camera
from plotting import *

load("coreclr")
import clr
clr.AddReference('/Users/cameronoscarmichie/Documents/GitHub/MAMOC/ReactionDiffusionLibrary/bin/Debug/net7.0/ReactionDiffusionLibrary.dll')
import ReactionDiffusionLibrary

gridxsize = 100
gridysize = 100

Prey_E0 = 50
Prey_EP = 1
Prey_N = 1000

Pred_E0 = 200
Pred_EP = 3
Pred_N = 1000
    
TheGrid = ReactionDiffusionLibrary.Grid(gridxsize, gridysize)
Prey = ReactionDiffusionLibrary.Species("Prey", Prey_E0, Prey_EP, Prey_N, TheGrid)
Pred = ReactionDiffusionLibrary.Species("Predator", Pred_E0, Pred_EP, Pred_N, TheGrid)


fig, ax = plt.subplots() 
cam = Camera(fig)
lastArr=[]

for i in range(500):
    Prey.Move()
    Pred.Move()
    TheGrid.Interact(Prey, Pred)
    fig, ax, lastArr = plot_imshow(fig, ax, lastArr)
    cam.snap()
    

plt.close()
ani= cam.animate(interval = 35)
ani.save('predatorprey_imshow.mp4')
plt.close()