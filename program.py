# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

class Human:
    def __init__(self, name = "Balder", damage = 75, health = 150):
        self.name = name
        self.damage = damage
        self.health = health

    def attack(self):
        print(f"{self.name} did {self.damage} damage!")

    def take_damage(self, damage_taken):
        self.health -= damage_taken
        print(f"{self.name} has taken {damage_taken} damage")
        print(f"{self.name} health is now {self.health}")

class Elf(Human):
    def __init__(self, name = "Solana", damage = 85, health = 100):
        super().__init__(name, damage, health)

class Orc(Human):
    def __init__(self, name = "Ugor", damage = 65, health = 175):
        super().__init__(name, damage, health)

class Wizard(Human):
    def __init__(self, name = "Iric", damage = 75, health = 125):
        super().__init__(name, damage, health)

class Dragon(Human):
    def __init__(self, name = "Alduin", damage = 25, health = 400):
        super().__init__(name, damage, health)

dragon_obj = Dragon()

dragon_obj.attack()
