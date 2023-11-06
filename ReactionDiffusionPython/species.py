import numpy as np
from typing import Dict, List
import random

class Species():
    def __init__(self, PredatorOrPrey: str, E_0: int, E_procreation: float, N: int, Grid_instance: object) -> None:
        self.pred_or_prey = PredatorOrPrey
        self.initial_energy = E_0
        self.min_procreation_energy = E_procreation
        self.num_agents = N
        self.agents : List[object] = []
        self.babies : List[object] = []
        self.death_list : List[object] = []
        
        self.grid = Grid_instance
        random.shuffle(self.grid.coords)
        self.species_coords = self.grid.coords[:self.num_agents]
        self.dying : bool = False  
        
    def move(self):
        if len(self.agents) < 1000: 
            self.dying = True
        else: 
            self.dying = False
        self.species_coords = [[0, 0]] * len(self.agents)
        
        for i, agent in enumerate(self.agents):
            dir_index = random.randint(0, 4)
            agent.move(self.grid.directions[dir_index])
            
            self.species_coords[i] = [agent.x, agent.y]
            agent.agent_index = i

            y_or_d_condition = ('y' if self.pred_or_prey == "Prey" else 'd')
            self.grid.animals_in_grid[agent.x][agent.y].append(f'{y_or_d_condition}{i}')
            ##self.grid.animals_in_grid = np.array(self.grid.animals_in_grid, dtype=object)

    def birth_babies(self):
        for baby in self.babies:
            self.agents.append(baby)
        self.babies : List[object] = []
    
    def kill_death_list(self):
        death_indices = [slain.agent_index for slain in self.death_list]
        for index in sorted(set(death_indices), reverse=True):
            del self.agents[index]
            del self.species_coords[index]
        
        self.num_agents-=len(death_indices)
        self.death_list : List[object] = []