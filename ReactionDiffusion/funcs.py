import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import pdist, squareform
from matplotlib.collections import LineCollection
import time 
from agent import Agent

def initialise_agents(species_instance: object):
    for i in range(species_instance.num_agents):
        this_agent = Agent(species_instance, i)
        species_instance.agents.append(this_agent)
        agent_x = species_instance.species_coords[i][0]
        agent_y = species_instance.species_coords[i][1]
        y_or_d_condition = ('y' if species_instance.pred_or_prey == "Prey" else 'd')
        species_instance.grid.animals_in_grid[agent_x][agent_y] = [f'{y_or_d_condition}{i}']

def filter_negative_pairs(array):
  xs, ys = [], []
  for pair in array:
    if pair[0] >= 0 and pair[1] >= 0:
      xs.append(int(pair[0]))
      ys.append(int(pair[1]))
  return xs, ys

def  plot_lines(Xs, Ys, ax, k, species):       
    # matrix of pairwise Euclidean distances
    all_coords = np.column_stack(Xs, Ys)
    distmat = squareform(pdist(all_coords, 'euclidean'))

    # select the kNN for each data point
    neighbors = np.sort(np.argsort(distmat, axis=1)[:, 1:k + 1])

    # get edge coordinates
    coordinates = np.zeros((len(all_coords), k, 2, 2))
    for i in range(len(all_coords)):
        for j in range(k):
            coordinates[i, j, :, 0] = np.array([all_coords[i, 0], all_coords[neighbors[i, j], 0]])
            coordinates[i, j, :, 1] = np.array([all_coords[i, 1], all_coords[neighbors[i, j], 1]])

    if species == "prey":
        lines = LineCollection(coordinates.reshape((len(all_coords) * k, 2, 2)), color='green', alpha=0.5)
    if species == "pred":
        lines = LineCollection(coordinates.reshape((len(all_coords) * k, 2, 2)), color='red', alpha=0.5)
    ax.add_collection(lines)
    return ax 

def plot_frame(fig, ax, Prey, Pred, k=0):
    gridxsize, gridysize = Prey.grid.gridxsize, Prey.grid.gridysize
    x_prey, y_prey = filter_negative_pairs(Prey.species_coords)
    x_pred, y_pred = filter_negative_pairs(Pred.species_coords)
    prey_scatter = ax.scatter(x_prey, y_prey, c='green', alpha=0.85)
    pred_scatter = ax.scatter(x_pred, y_pred, c='red', alpha=0.85)

    if k>1:
        ax = plot_lines(x_prey, y_prey, ax, k, "prey")
        ax = plot_lines(x_pred, y_pred, ax, k, "pred")

    ax.set(xlim=(0, gridxsize), ylim=(0, gridysize))
    plt.axis('off')
    return fig, ax

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

def plot_imshow(fig, ax, TheGrid):
    arr = process_data_for_imshow(TheGrid.animals_in_grid)
    ax.imshow(arr)
    ax.axis('off')
    return fig, ax

def timeme(method):
    def wrapper(*args, **kw):
        startTime = int(round(time.time() * 1000))
        result = method(*args, **kw)
        endTime = int(round(time.time() * 1000))
        print(endTime - startTime,'ms')
        return result
    return wrapper

def procreate(species_list, species_obj):
    for i in range(0, len(species_list)-1, 2):
        pred_mum = species_obj.agents[species_list[i]]
        pred_dad = species_obj.agents[species_list[i+1]]
        pred_mum.energy-=len(species_list)
        pred_dad.energy-=len(species_list)
        if pred_mum.energy + pred_dad.energy > pred_mum.min_procreation_energy:
            pred_mum.procreate(pred_dad)

def single_procreation(agent_id, species_obj):
    single_mum = species_obj.agents[agent_id]
    if single_mum.energy > species_obj.min_procreation_energy:
        single_mum.procreate(single_mum)


@timeme
def interact(Prey_species_obj, Pred_species_obj, Grid_obj):
    for y_i in range(Grid_obj.gridysize):
        for x_i in range(Grid_obj.gridxsize):

            if not Grid_obj.animals_in_grid[y_i][x_i]: pass
            preys, preds = [], []
            
            for agent_str in Grid_obj.animals_in_grid[y_i][x_i]:
                if agent_str[0] == 'y': preys.append(int(agent_str[1:]))
                if agent_str[0] == 'd': preds.append(int(agent_str[1:]))
                if not preys or not preds: pass

                # Predators breed and feed on prey
                procreate(preds, Pred_species_obj)
                for i in range(len(preds)):
                    if i < len(preys):
                        predator = Pred_species_obj.agents[preds[i]]
                        food = Prey_species_obj.agents[preys[i]]
                        predator.energy+=food.energy
                        food.add_to_death_list()
                            
                # Preys procreate
                procreate(preys, Prey_species_obj) 

                if Prey_species_obj.dying and len(preys) == 1:
                    single_procreation(preys[0], Prey_species_obj)
                if Pred_species_obj.dying and len(preds) == 1:
                    single_procreation(preds[0], Pred_species_obj)
 

    # At the end of the turn make babies into adults
    Prey_species_obj.birth_babies()
    Pred_species_obj.birth_babies()
    
    # and kill those on death list
    Prey_species_obj.kill_death_list()
    Pred_species_obj.kill_death_list()
