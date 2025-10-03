from Enemy import *
import random

class Ogre(Enemy):
    def __init__(self,health_points: int =  10,attack_damage: int = 1):
        self.attack_damage = attack_damage
        self.health_points = health_points
        super().__init__("Ogre",health_points,attack_damage)


    def talk(self):
        print(f"{self.get_type_of_enemy()} says 'Ogreeeee!'")
    
    def attack(self):
        print(f"{self.get_type_of_enemy()} attacks for {self.attack_damage} damage")

        
    def special_attack(self):
        did_special_attack_work = random.random() < 0.20
        if did_special_attack_work:
            self.attack_damage += 4

        print(f"{self.get_type_of_enemy()} uses special attack for {self.attack_damage} damage")