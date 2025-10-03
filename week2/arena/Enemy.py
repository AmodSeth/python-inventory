class Enemy:
    type_of_enemy: str
    health_points: int = 10
    attack_damage: int = 1
 
    # def __init__(self): #this is automatically gets created
    #     pass


    ## paramterized constructor we can pass arguments to the constructor i.e we can overwrite the default values
    def __init__(self, type_of_enemy: str, health_points: int =  10, attack_damage: int = 1):
        self.__type_of_enemy = type_of_enemy
        self.health_points = health_points
        self.attack_damage = attack_damage

    def get_type_of_enemy(self):
        return self.__type_of_enemy


    def special_attack(self):
        return "Enemy has not special attack"







    def talk(self):
        # abtraction: we use the functionality of the Enemy class without knowing what it is
        print(f"{self.__type_of_enemy} says 'Hello!'")

    def attack(self):
        print(f"{self.__type_of_enemy} attacks for {self.attack_damage} damage")

    def walk_forward(self):
        print(f"{self.__type_of_enemy} walks forward closer to the player")
