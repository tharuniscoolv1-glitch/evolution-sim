from creature import Creature 
import statistics

class World:

    def __init__(self, width, height, population : list):
        self.width = width
        self.height = height
        self.population = []

        for i in population:
            creature = Creature(
                health = 100,
                speed = 10,
                mut_chance = 1,
                appetite = 100,
            range = 5
            )

            self.population.append(c)

    def update(self):

        for creature in self.population[:]:
            baby = creature.new_day(cutoff=self.current_cutoff , return_baby=True)

            if baby:
                self.population.append(baby)
        self.remove_dead_creatures()
    
    def remove_dead_creatures(self):
        alive = [ creature for creature in self.population if not creature.is_dead()]
        self.population = alive
        
                
    def display_population(self):
        print('population:', len(self.population))


    @property
    def current_cutoff(self):
        if not self.population:    
            return 0 

        fitness = [c.speed*c.range for c in self.population]

        average_fitness = statistics.mean(fitness)

        cutoff = average_fitness
        return cutoff 



    
    
   










