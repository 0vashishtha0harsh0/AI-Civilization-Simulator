import pygame
import random

from src.constants import TILE_SIZE


class Citizen:

    def __init__(self, world):

        self.world = world

        self.health = 100
        self.hunger = 100
        self.energy = 100

        while True:

            row = random.randint(0, len(world.grid) - 1)
            col = random.randint(0, len(world.grid[0]) - 1)

            if world.grid[row][col] != 2:
                break

        self.row = row
        self.col = col

        self.move_timer = 0

    def update(self):

        self.move_timer += 1

        if self.move_timer < 15:
            return

        self.move_timer = 0

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        dr, dc = random.choice(directions)

        new_row = self.row + dr
        new_col = self.col + dc

        rows = len(self.world.grid)
        cols = len(self.world.grid[0])

        if 0 <= new_row < rows and 0 <= new_col < cols:

            if self.world.grid[new_row][new_col] != 2:
                self.row = new_row
                self.col = new_col

    def draw(self, screen):

        x = self.col * TILE_SIZE + TILE_SIZE // 2
        y = self.row * TILE_SIZE + TILE_SIZE // 2

        pygame.draw.circle(
            screen,
            (255, 0, 0),
            (x, y),
            TILE_SIZE // 3
        )