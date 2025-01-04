import random
from .cell import CellType
from .cell import Cell

class Organism:
    def __init__(self, grid, cells):
        self.grid = grid
        self.cells = cells  # List of (x, y, CellType) tuples
        self.energy = 100
        self.food_eaten = 0
        
    def update(self):
        # Process each cell's behavior
        for x, y, cell_type in self.cells:
            if cell_type == CellType.MOUTH:
                self._process_mouth(x, y)
            elif cell_type == CellType.PRODUCER:
                self._process_producer(x, y)
            elif cell_type == CellType.MOVER:
                self._process_mover(x, y)
            elif cell_type == CellType.KILLER:
                self._process_killer(x, y)
            elif cell_type == CellType.BUILDER:
                self._process_builder(x, y)

        self.energy -= len(self.cells) * 0.7
        if self.energy <= 0:
            self._die()

    def _die(self):
        for c in self.cells:
            self.grid.set_cell(c[0], c[1], Cell(CellType.EMPTY))

    def _process_mouth(self, x, y):
        for (adj_x, adj_y), cell in self.grid.get_adjacent_cells(x, y):
            if cell.type == CellType.FOOD:
                self.energy += 1
                self.food_eaten += 1
                self.grid.set_cell(adj_x, adj_y, Cell())

    def _process_producer(self, x, y):
        for (adj_x, adj_y), cell in self.grid.get_adjacent_cells(x, y):
            if cell.type == CellType.EMPTY and random.random() < 0.1:
                self.grid.set_cell(adj_x, adj_y, Cell(CellType.FOOD))

    def _process_mover(self, x, y):
        if random.random() < 0.2:  # 20% chance to move each tick
            # Choose random direction
            dx = random.choice([-1, 0, 1])
            dy = random.choice([-1, 0, 1])
            
            # Calculate new positions for all cells
            new_positions = [
                (cell_x + dx, cell_y + dy, cell_type)
                for cell_x, cell_y, cell_type in self.cells
            ]
            
            # Check if movement is valid
            can_move = True
            for new_x, new_y, _ in new_positions:
                # Check boundaries
                if not (0 <= new_x < self.grid.width and 0 <= new_y < self.grid.height):
                    can_move = False
                    break
                
                # Get cell at new position
                target_cell = self.grid.get_cell(new_x, new_y)
                
                # Check if target cell is occupied by something other than our own cells
                if (target_cell.type != CellType.EMPTY and 
                    not any(x == new_x and y == new_y for x, y, _ in self.cells)):
                    can_move = False
                    break
            
            # If movement is valid, update organism position
            if can_move:
                # Clear old positions
                for old_x, old_y, _ in self.cells:
                    self.grid.set_cell(old_x, old_y, Cell(CellType.EMPTY))
                
                # Update cells list with new positions
                self.cells = new_positions
                
                # Set new positions in grid
                for new_x, new_y, cell_type in new_positions:
                    new_cell = Cell(cell_type)
                    new_cell.organism = self
                    self.grid.set_cell(new_x, new_y, new_cell)
                
                # Movement costs energy
                self.energy -= 1

    def _process_killer(self, x, y):
        for (adj_x, adj_y), cell in self.grid.get_adjacent_cells(x, y):
            if cell.organism:
                if cell.organism != self:
                    if not any(c[2] == CellType.ARMOR for c in cell.organism.cells):
                        cell.organism.energy -= 20
            elif cell.type == CellType.WALL:
                self.grid.set_cell(adj_x, adj_y, Cell(CellType.EMPTY))

    def _process_builder(self, x, y):
        for (adj_x, adj_y), cell in self.grid.get_adjacent_cells(x, y):
            if cell.type == CellType.EMPTY and random.random() < 0.05:
                self.grid.set_cell(adj_x, adj_y, Cell(CellType.WALL))

    def _mutate(self, cells):
        mutation_type = random.choice(['change', 'lose', 'add'])
        
        if mutation_type == 'change':
            # Change a random cell to a random type
            if cells:
                idx = random.randrange(len(cells))
                x, y, _ = cells[idx]
                new_type = random.choice([
                    CellType.MOUTH, CellType.PRODUCER, CellType.MOVER,
                    CellType.KILLER, CellType.ARMOR, CellType.BUILDER
                ])
                cells[idx] = (x, y, new_type)
                
        elif mutation_type == 'lose':
            # Remove a random cell
            if len(cells) > 1:  # Keep at least one cell
                idx = random.randrange(len(cells))
                cells.pop(idx)
                
        elif mutation_type == 'add':
            # Add a cell adjacent to an existing one
            if cells:
                # Select random existing cell
                base_x, base_y, _ = random.choice(cells)
                
                # Get possible adjacent positions
                adjacent_positions = [
                    (base_x + dx, base_y + dy)
                    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]
                ]
                
                # Filter valid positions (within grid and not already in cells)
                valid_positions = [
                    (x, y) for x, y in adjacent_positions
                    if (0 <= x < self.grid.width and 0 <= y < self.grid.height and
                        not any(x == cx and y == cy for cx, cy, _ in cells))
                ]
                
                if valid_positions:
                    new_x, new_y = random.choice(valid_positions)
                    new_type = random.choice([
                        CellType.MOUTH, CellType.PRODUCER, CellType.MOVER,
                        CellType.KILLER, CellType.ARMOR, CellType.BUILDER
                    ])
                    cells.append((new_x, new_y, new_type))

    def reproduce(self):
        # Clone current cells
        offspring_cells = self.cells.copy()
        
        # Apply mutation
        if random.random() < 0.2:
            self._mutate(offspring_cells)
        
        # Calculate minimum safe distance
        max_organism_dimension = max(
            max(abs(x1 - x2) for x1, y1, _ in self.cells for x2, y2, _ in self.cells),
            max(abs(y1 - y2) for x1, y1, _ in self.cells for x2, y2, _ in self.cells)
        ) + 1

        # Choose random direction and distance
        direction = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
        distance = max_organism_dimension + random.randint(1, 3)
        
        # Calculate offspring position
        base_x = self.cells[0][0]  # Use first cell as reference
        base_y = self.cells[0][1]
        offset_x = direction[0] * distance
        offset_y = direction[1] * distance
        
        # Translate all cells to new position
        translated_cells = [
            (x + offset_x, y + offset_y, cell_type)
            for x, y, cell_type in offspring_cells
        ]
        
        # Check if reproduction is possible (all cells are empty)
        for x, y, _ in translated_cells:
            if not (0 <= x < self.grid.width and 0 <= y < self.grid.height):
                return False  # Out of bounds
            cell = self.grid.get_cell(x, y)
            if cell.type != CellType.EMPTY:
                return False  # Space occupied
        
        # Create offspring
        offspring = Organism(self.grid, translated_cells)
        
        # Place offspring in grid
        for x, y, cell_type in translated_cells:
            new_cell = Cell(cell_type)
            new_cell.organism = offspring
            self.grid.set_cell(x, y, new_cell)
        
        return offspring