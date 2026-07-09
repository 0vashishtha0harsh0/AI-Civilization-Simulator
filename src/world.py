import random
import pygame

from src.constants import ROWS, COLS, TILE_SIZE


class World:

    def __init__(self):
        self.grid = []
        self.generate()

    def generate(self):
        self.grid = []

        for row in range(ROWS):

            current_row = []

            for col in range(COLS):

                chance = random.randint(1, 100)

                if chance <= 10:
                    tile = 1  # Tree

                elif chance <= 15:
                    tile = 2  # Water

                elif chance <= 20:
                    tile = 3  # Stone

                elif chance <= 25:
                    tile = 4  # Food

                else:
                    tile = 0  # Empty

                current_row.append(tile)

            self.grid.append(current_row)

    def find_nearest_food(self, row, col):

        nearest = None
        min_distance = float("inf")

        for r in range(len(self.grid)):
            for c in range(len(self.grid[0])):

                if self.grid[r][c] == 4:

                    distance = abs(row - r) + abs(col - c)

                    if distance < min_distance:
                        min_distance = distance
                        nearest = (r, c)

        return nearest

    def remove_food(self, row, col):
        self.grid[row][col] = 0

    def draw(self, screen):

        for row in range(ROWS):
            for col in range(COLS):

                x = col * TILE_SIZE
                y = row * TILE_SIZE

                tile = self.grid[row][col]

                if tile == 0:
                    color = (30, 30, 30)        # Empty

                elif tile == 1:
                    color = (34, 139, 34)       # Tree

                elif tile == 2:
                    color = (0, 191, 255)       # Water

                elif tile == 3:
                    color = (130, 130, 130)     # Stone

                elif tile == 4:
                    color = (255, 215, 0)       # Food

                pygame.draw.rect(
                    screen,
                    color,
                    (x, y, TILE_SIZE, TILE_SIZE)
                )

                pygame.draw.rect(
                    screen,
                    (40, 40, 40),
                    (x, y, TILE_SIZE, TILE_SIZE),
                    1
                )