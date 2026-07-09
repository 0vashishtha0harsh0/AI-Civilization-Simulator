import pygame

from src.constants import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from src.world import World


def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("AI Civilization Simulator")

    clock = pygame.time.Clock()

    world = World()

    running = True

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))

        world.draw(screen)

        pygame.display.flip()

        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()