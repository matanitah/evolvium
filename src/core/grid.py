import numpy as np
from .cell import Cell, CellType

class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[Cell() for _ in range(width)] for _ in range(height)]

    def get_cell(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.grid[y][x]
        return None

    def set_cell(self, x, y, cell):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.grid[y][x] = cell

    def get_adjacent_cells(self, x, y):
        adjacent = []
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            cell = self.get_cell(x + dx, y + dy)
            if cell:
                adjacent.append(((x + dx, y + dy), cell))
        return adjacent