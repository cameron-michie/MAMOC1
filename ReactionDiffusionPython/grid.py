import numpy as np
from typing import Dict, List
import random

class Grid:
    def __init__(self, max_x: int, max_y: int) -> None:
        self.gridxsize = max_x
        self.gridysize = max_y
        self.generate_coords()
        self.animals_in_grid = [[[] for _ in range(max_y)] for _ in range(max_x)]
        self.directions = ["LEFT", "RIGHT", "UP", "DOWN", "STAY"]
        
    def generate_coords(self) -> None:
        xcoords = [i for i in range(self.gridxsize)]
        ycoords = [i for i in range(self.gridysize)]
        random.shuffle(xcoords)
        random.shuffle(ycoords) 
        self.coords = [[x,y] for x in xcoords for y in ycoords]
        random.shuffle(self.coords)