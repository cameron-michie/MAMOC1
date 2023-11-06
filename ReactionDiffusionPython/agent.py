import numpy as np
from typing import Dict, List
from species import Species

class Agent(Species):
    
    def __init__(self, species: object, agent_number: int, energy=None) -> None:
        super().__init__(species.pred_or_prey, 
                         species.initial_energy, 
                         species.min_procreation_energy, 
                         species.num_agents, 
                         species.grid)
        self.parent_species = species

        y_or_d_condition = ('y' if self.pred_or_prey == "Prey" else 'd')
        self.agent_id = f"{y_or_d_condition}{agent_number}"
        self.agent_index = agent_number

        self.x = self.parent_species.species_coords[agent_number][0]
        self.y = self.parent_species.species_coords[agent_number][1]

        if energy is not None:  self.energy = energy
        else: self.energy = np.random.normal(species.initial_energy, species.initial_energy/3)

        self.step_size = 1
            
    def add_to_death_list(self):
        self.parent_species.death_list.append(self)
        
    def procreate(self, other):

        Baby = Agent(self.parent_species, 
                     self.agent_index, 
                     energy=(self.energy + other.energy)/2)

        self.energy = 1 * self.energy / 2
        other.energy = 1 * other.energy / 2

        self.parent_species.babies.append(Baby)
   
    
    def move(self, direction : str):
        step = 1 ##round(self.step_size * self.energy / 100 + 0.6)
        # Change agent x and y coords
        self.energy -=step
        if direction == "LEFT":
            self.x += -step if self.x - step > 0 else +step
        if direction == "RIGHT":
            self.x += step if self.x + step < self.grid.gridxsize-1 else -step
        if direction == "UP":
            self.y += step if self.y + step < self.grid.gridysize-1 else -step
        if direction == "DOWN":
            self.y += -step if self.y - step > 0 else +step
        if direction == "STAY":
            if self.pred_or_prey == "Prey": self.energy += 10
            if self.pred_or_prey == "Pred": self.energy += 4

        # Kill if no energy
        if self.energy <= 0: self.add_to_death_list() 