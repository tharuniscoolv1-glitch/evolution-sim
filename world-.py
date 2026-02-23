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
                appetite = 100,
            range_ = 5, score = 0
            )

            self.population.append(c)

    def update(self):
        for creature in self.population:
            creature.update()

    def display_population(self):
        print('population:', len(self.population))

    def get_cutoff(self):
        if not self.population:    
            return 0 

        fitness = [c.speed*c.range for c in self.population]

        average_fitness = statistics.mean(fitness)

        cutoff = average_fitness*1.5
        return cutoff 

    def speed_scoring(self):
        cutoff = self.get_cutoff()

        for Creature in self.population:
            if c.speed*c.range > cutoff:
                c.score = c.score + 1


    
    
   









