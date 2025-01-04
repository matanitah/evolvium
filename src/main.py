import pygame
import sys
from config.settings import GRID_WIDTH, GRID_HEIGHT, SIMULATION_SPEED
from core.simulation import Simulation
from visualization.renderer import Renderer

def main():
    print(f"GRID WIDTH: {GRID_WIDTH}")
    print(f"GRID WIDTH: {GRID_HEIGHT}")

    simulation = Simulation(GRID_WIDTH, GRID_HEIGHT)
    renderer = Renderer(GRID_WIDTH, GRID_HEIGHT)
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        simulation.update()
        renderer.render(simulation.grid)
        clock.tick(SIMULATION_SPEED)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()