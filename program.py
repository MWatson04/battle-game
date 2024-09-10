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

class Game:
    def __init__(self, game_over = False, state_one_over = False, chosen_class = None):
        self.game_over = game_over
        self.state_one_over = state_one_over
        self.chosen_class = chosen_class

    def game_setup(self):
        valid_choice = False
        print("Welcome to Battle Game")

        while not valid_choice:
            print("")
            print("Please select your class to start")
            print("1)   Human")
            print("2)   Elf")
            print("3)   Orc")
            print("4)   Wizard")

            class_input = input("Enter the number or name of a class to make your choice: ").lower()

            if class_input in ("1", "human"):
                self.chosen_class = Human()
                print(f"You have chosen the human class. Your name is {self.chosen_class.name}!")
                print(f"Your Health is: {self.chosen_class.health}")
                print(f"Your Attack Damage is: {self.chosen_class.damage}")
                valid_choice = True
            elif class_input in ("2", "elf"):
                self.chosen_class = Elf()
                print(f"You have chosen the elf class. Your name is {self.chosen_class.name}!")
                print(f"Your Health is: {self.chosen_class.health}")
                print(f"Your Attack Damage is: {self.chosen_class.damage}")
                valid_choice = True
            elif class_input in ("3", "orc"):
                self.chosen_class = Orc()
                print(f"You have chosen the orc class. Your name is {self.chosen_class.name}!")
                print(f"Your Health is: {self.chosen_class.health}")
                print(f"Your Attack Damage is: {self.chosen_class.damage}")
                valid_choice = True
            elif class_input in ("4", "wizard"):
                self.chosen_class = Wizard()
                print(f"You have chosen the wizard class. Your name is {self.chosen_class.name}!")
                print(f"Your Health is: {self.chosen_class.health}")
                print(f"Your Attack Damage is: {self.chosen_class.damage}")
                valid_choice = True
            else:
                print("Invalid choice. Choose again")

def run_game():
    game_obj = Game()

    game_obj.game_setup()

run_game()
