import pygame
import sys
from config.settings import GRID_WIDTH, GRID_HEIGHT, SIMULATION_SPEED
from core.simulation import Simulation
from visualization.renderer import Renderer

def main():
    simulation = Simulation(GRID_WIDTH, GRID_HEIGHT)
    renderer = Renderer(GRID_WIDTH, GRID_HEIGHT)
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    simulation.initialize()  # Reinitialize the simulation


        simulation.update()
        renderer.render(simulation.grid)
        clock.tick(SIMULATION_SPEED)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()