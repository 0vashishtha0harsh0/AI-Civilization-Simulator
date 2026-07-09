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

            row = random.randint(0, len(world.grid)-1)
            col = random.randint(0, len(world.grid[0])-1)

            if world.grid[row][col] != 2:
                break

        self.row = row
        self.col = col

        self.move_timer = 0

    def update(self):

        self.move_timer += 1

        if self.move_timer < 10:
            return

        self.move_timer = 0

        self.hunger -= 1

        if self.hunger <= 30:

            target = self.world.find_nearest_food(
                self.row,
                self.col
            )

            if target:

                tr, tc = target

                if self.row < tr:
                    self.row += 1

                elif self.row > tr:
                    self.row -= 1

                elif self.col < tc:
                    self.col += 1

                elif self.col > tc:
                    self.col -= 1

                if self.row == tr and self.col == tc:

                    self.world.remove_food(tr, tc)

                    self.hunger = 100

        else:

            directions = [
                (-1,0),
                (1,0),
                (0,-1),
                (0,1)
            ]

            dr,dc = random.choice(directions)

            nr = self.row + dr
            nc = self.col + dc

            rows = len(self.world.grid)
            cols = len(self.world.grid[0])

            if 0<=nr<rows and 0<=nc<cols:

                if self.world.grid[nr][nc] != 2:
                    self.row = nr
                    self.col = nc

    def draw(self,screen):

        x = self.col*TILE_SIZE + TILE_SIZE//2
        y = self.row*TILE_SIZE + TILE_SIZE//2

        pygame.draw.circle(
            screen,
            (255,0,0),
            (x,y),
            TILE_SIZE//3
        )