import random
import statistics


class Creature:

    def __init__(self , health=100 , speed=10 , mut_chance=1, appetite=100, range =5):
        
        self.health = health
        self.speed = speed
        self.mut_chance = mut_chance
        self.appetite = appetite
        self.range = range

    def reproduce(self , return_baby=False):


        baby_health = self.health
        baby_speed = self.speed
        baby_mut_chance = self.mut_chance
        
        if self.mut_chance >= random.randint(0 , 100):
            a = random.randint(1 ,3)
            if a == 1:
                baby_health = max(1 , (baby_health + random.randint(-2 , 2)))

            
            elif a == 2:
                baby_speed = max(1 , (baby_speed + random.randint(-2 , 2)))

            else:
                baby_mut_chance = max(1 , (baby_mut_chance + random.randint(-1 , 1)))           
            
        baby = Creature(health=baby_health , speed=baby_speed , mut_chance=baby_mut_chance)

        self.appetite -= 40
        if return_baby:
            return baby


    def eat(self , cutoff):
        can_eat = False
        can_eat_twice = False

        if self.speed * self.range > cutoff:
            can_eat = True

        if self.speed * self.range > (cutoff * 1.5):
            can_eat_twice = True

        if can_eat_twice:
            self.appetite = min(100 , self.appetite + 40)

        elif can_eat:
            self.appetite = min(100 , self.appetite + 20)

    

    def new_day(self , cutoff , return_baby=False):
        baby = None
        self.appetite -= 20
        self.eat(cutoff=cutoff)

        if self.appetite > 80:
            baby = self.reproduce(return_baby=return_baby)

        if return_baby:
            return baby
        


            