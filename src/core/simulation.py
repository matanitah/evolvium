import random
from .grid import Grid
from .organism import Organism
from .cell import CellType
from .cell import Cell

class Simulation:
    def __init__(self, width, height):
        self.grid = Grid(width, height)
        self.organisms = []
        self.initialize()

    def initialize(self):
        # Add some initial food
        for _ in range(self.grid.width * self.grid.height // 10):
            x = random.randint(0, self.grid.width - 1)
            y = random.randint(0, self.grid.height - 1)
            self.grid.set_cell(x, y, Cell(CellType.FOOD))

        # Add some initial organisms
        for _ in range(10):
            self.spawn_random_organism()

    def spawn_random_organism(self):
        x = random.randint(0, self.grid.width - 1)
        y = random.randint(0, self.grid.height - 1)
        
        # Create a simple organism with basic cells
        cells = [
            (x, y, CellType.MOUTH),
            (x+1, y, CellType.PRODUCER),
            (x, y+1, CellType.MOVER)
        ]
        
        organism = Organism(self.grid, cells)
        self.organisms.append(organism)

    def update(self):
        # Create a list for new organisms
        new_organisms = []
        
        # Update all organisms
        for organism in self.organisms[:]:  # Create a copy of the list to iterate
            organism.update()
            
            # Check reproduction
            if organism.food_eaten >= len(organism.cells):
                offspring = organism.reproduce()
                if offspring:
                    new_organisms.append(offspring)
            
            # Remove dead organisms
            if organism.energy <= 0:
                # Remove organism cells from grid
                for x, y, _ in organism.cells:
                    self.grid.set_cell(x, y, Cell())
                self.organisms.remove(organism)

        # Add new organisms
        self.organisms.extend(new_organisms)

        # Spawn new food randomly
        if random.random() < 0.1:
            x = random.randint(0, self.grid.width - 1)
            y = random.randint(0, self.grid.height - 1)
            if self.grid.get_cell(x, y).type == CellType.EMPTY:
                self.grid.set_cell(x, y, Cell(CellType.FOOD))