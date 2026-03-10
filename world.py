

from creature import Creature 
import statistics
import time
class World:

    def __init__(self, width, height, population):
        

        self.width = width
        self.height = height
        self.population = []

        
    
        for i in range(population):
                creature = Creature(
                    health = 100,
                    speed = 10,
                    mut_chance = 1,
                    appetite = 100,
                    range = 5,
                )
                self.population.append(creature)
        
            


    def update(self):
        
        for creature in self.population[:]:
            baby = creature.new_day(cutoff=self.current_cutoff, return_baby=True)

            if baby:
                self.population.append(baby)
        self.remove_dead_creatures()

    def run(self, days=50, sleep_time=0.1):

        print("starting simulation")

        for day in range(1, days + 1):

            if not self.population:
                print("all creatures died on day", day-1)
                break

            self.update()

            print(f"day {day} - population:", len(self.population))

            if sleep_time:
                time.sleep(sleep_time)

        print("simulation ended")

        

    
    def remove_dead_creatures(self):
    
        alive = [c for c in self.population if not c.is_dead()]
        self.population = alive


    def display_population(self):
        print('population:', len(self.population), end=' - ')

    @property
    def current_cutoff(self):    
        if not self.population:
            return 0
        fitness = [c.speed * c.range for c in self.population]
        average_fitness = statistics.mean(fitness)

        cutoff = average_fitness * 1.3
        return cutoff



