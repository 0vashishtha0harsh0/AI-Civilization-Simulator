from src.citizen import Citizen


class Simulation:

    def __init__(self, world):

        self.world = world

        self.citizens = []

        for _ in range(100):
            self.citizens.append(Citizen(world))

    def update(self):

        for citizen in self.citizens:
            citizen.update()

    def draw(self, screen):

        for citizen in self.citizens:
            citizen.draw(screen)