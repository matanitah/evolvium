import pygame
from config.settings import COLORS, CELL_SIZE

class Renderer:
    def __init__(self, width, height):
        pygame.init()
        self.width = width * CELL_SIZE
        self.height = height * CELL_SIZE
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Evolvium")

    def render(self, grid):
        self.screen.fill((0, 0, 0))
        
        for y in range(grid.height):
            for x in range(grid.width):
                cell = grid.get_cell(x, y)
                color = COLORS.get(cell.type.name, (0, 0, 0))
                
                pygame.draw.rect(
                    self.screen,
                    color,
                    (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                )
        
        pygame.display.flip()