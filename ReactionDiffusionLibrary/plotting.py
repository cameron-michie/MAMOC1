import numpy as np
import json


def plot_imshow(fig, ax, lastArr=[]):
    f = open('agentsInGrid.json')
    data = json.load(f)
    arr = process_data_for_imshow(data)
    if len(lastArr)>1:
        ax.imshow(lastArr, alpha=0.7)
    ax.imshow(arr)
    ax.axis('off')
    return fig, ax, arr

def process_data_for_imshow(arr):
    color_map = {'y': (0.1, 0.7, 0.1),  
                'd': (0.8, 0, 0)}  
    colors = []

    for row in arr:
        color_row = []
        for item in row:
            if len(item) > 0:
                char = item[0][0]
                if char in color_map:
                    color = color_map[char]
                else: color = (1,1,1)
            else: color = (1,1,1)  
            color_row.append(color)
        colors.append(color_row)
    colors_array = np.array(colors, dtype=np.float32)

    return colors_array
