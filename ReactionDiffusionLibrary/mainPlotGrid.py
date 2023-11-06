from pythonnet import load
import numpy as np
import matplotlib.pyplot as plt
from celluloid import Camera
from plotting import *
from moviepy.editor import VideoFileClip, clips_array


load("coreclr")
import clr
clr.AddReference('/Users/cameronoscarmichie/Documents/GitHub/MAMOC/ReactionDiffusionLibrary/bin/Debug/net7.0/ReactionDiffusionLibrary.dll')
import ReactionDiffusionLibrary

with open("PopulationData.txt", 'w') as file:
    pass
videos = [] 
def combine_videos_in_grid(videos, output_file):
    # Load all video clips
    clips = [VideoFileClip(vid) for vid in videos]

    # Ensure that all video clips have the same duration as the shortest clip
    min_duration = min(clip.duration for clip in clips)
    clips = [clip.subclip(0, min_duration) for clip in clips]

    # Arrange video clips into a 3x3 grid
    final_clip = clips_array([[clips[0], clips[1], clips[2]],
                              [clips[3], clips[4], clips[5]],
                              [clips[6], clips[7], clips[8]]])

    # Write the result to an output file
    final_clip.write_videofile(output_file, codec='libx264')

def LoopModel(Prey_EP, Pred_EP):
    gridxsize = 200
    gridysize = 200

    Prey_E0 = 200
    Prey_N = 3000

    Pred_E0 = 200
    Pred_N = 3000

    TheGrid = ReactionDiffusionLibrary.Grid(gridxsize, gridysize)
    Prey = ReactionDiffusionLibrary.Species("Prey", Prey_E0, Prey_EP, Prey_N, TheGrid)
    Pred = ReactionDiffusionLibrary.Species("Predator", Pred_E0, Pred_EP, Pred_N, TheGrid)


    fig, ax = plt.subplots() 
    cam = Camera(fig)
    lastArr=[]

    for i in range(1500):
        Prey.Move()
        Pred.Move()
        TheGrid.Interact(Prey, Pred)
        fig, ax, lastArr = plot_imshow(fig, ax, lastArr)
        plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
        cam.snap()
        
    TheGrid.SaveLineToFile(f"\nand all of that ^^^ was prey{Prey_EP} pred{Pred_EP}\n\n\n\n\n")
    plt.close()
    ani= cam.animate(interval = 35)
    ani.save(f'prey{Prey_EP} pred{Pred_EP}.mp4')
    plt.close()

for i in (1, 25, 50):
    for j in (1, 25, 50):
        LoopModel(i, j)
        videos.append(f'prey{i} pred{j}.mp4')

combine_videos_in_grid(videos, "OutputGridVideo.mp4")