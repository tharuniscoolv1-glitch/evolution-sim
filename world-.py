from creature import Creature 

class World:

    def __init__(self, width, height, banana_population):
        self.width = width
        self.height = height
        self.population = population = [] 

        for i in range(banana_population):
            creature = Creature(
                health = 100,
                speed = 10,
                mut_chance = 1,
                appetite = 100)

            self.population.append(creature)

    def update(self):
        for creature in self.population:
            creature.update()

    def display_population(self):
        print('population size', len(self.population))
   




