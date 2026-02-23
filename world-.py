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

        average_speed = statistics.mean(fitness)

        cutoff = average_speed*1.5
        return cutoff 

    def speed_scoring(self):
        cutoff = self.get_cutoff()

        for creature in self.population:
            if creature.speed*creature.range > cutoff:
                creature.score = creature.score + 1


    
    
   








