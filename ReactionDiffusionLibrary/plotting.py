import numpy as np
import json

def plot_imshow(fig, ax, lastArr=[]):
    f = open('animals_in_grid.json')
    data = json.load(f)
    arr = process_data_for_imshow(data)
    if len(lastArr)>1:
        lastArr = brighten_image(lastArr, 5)
        ax.imshow(lastArr, alpha=1)
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

def brighten_image(image_data, brightness_factor):
    brightened_image_data = []
    
    for row in image_data:
        brightened_row = []
        
        for pixel in row:
            r, g, b = pixel
            
            r_bright = min(int(r * brightness_factor), 255)
            g_bright = min(int(g * brightness_factor), 255)
            b_bright = min(int(b * brightness_factor), 255)
            
            brightened_pixel = (r_bright, g_bright, b_bright)
            brightened_row.append(brightened_pixel)

        brightened_image_data.append(brightened_row)
    
    return brightened_image_data