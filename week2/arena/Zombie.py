from Enemy import *
import random

class Zombie(Enemy):
    def __init__(self,
                health_points: int =  10,
                attack_damage: int = 1):
        super().__init__("Zombie",health_points,attack_damage)


    def talk(self):
        print(f"{self.get_type_of_enemy()} says 'Hello!'")

    
    def attack(self):
        print(f"{self.get_type_of_enemy()} attacks for {self.attack_damage} damage")

    def special_attack(self):
        did_special_attack_work = random.random() < 0.50
        if did_special_attack_work:
            self.health_points += 2

        print(f"{self.get_type_of_enemy()} uses special attack and gains 2 health points to {self.health_points} health points")

        
