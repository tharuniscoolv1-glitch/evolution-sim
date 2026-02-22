from creature import Creature 
import statistics

class World:

    def __init__(self, width, height, population):
        self.width = width
        self.height = height
        self.population = [] 

        for i in range(population):
            c = Creature(
                health = 100,
                speed = 10,
                mut_chance = 1,
                appetite = 100)

            self.population.append(c)

    def update(self):
        for creature in self.population:
            creature.update()

    def display_population(self):
        print('population:', len(self.population))
   






