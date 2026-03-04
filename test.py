from creature import Creature 
import statistics

class World:

    def __init__(self, width, height, population : int):
        self.width = width
        self.height = height
        self.population = []

        for c in range(population):
            creature = Creature(
                health = 100,
                speed = 10,
                mut_chance = 10,
                appetite = 100,
            range = 5
            )

            self.population.append(creature)

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

        average_fitness = statistics.mean(fitness) * 0.8

        cutoff = average_fitness
        return cutoff 

new_world = World(5 , 5 , 150)

for i in range(15):
    new_world.update()
    new_world.display_population()

