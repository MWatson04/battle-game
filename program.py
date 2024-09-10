# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

import time
import random

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
    def __init__(self, game_over = False, chosen_class = None, enemy = Dragon()):
        self.game_over = game_over
        self.chosen_class = chosen_class
        self.enemy = enemy

    def display_options(self):
        print("")
        print("Please select your class to start")
        print("1)   Human")
        print("2)   Elf")
        print("3)   Orc")
        print("4)   Wizard")
        print("5    Exit")

    def make_choice(self):
        valid_choice = False
        class_input = input("Enter the number or name of a class to make your choice: ").lower()
    
        while not valid_choice:
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
            elif class_input in ("5", "exit"):
                print("Goodbye!")
                valid_choice = True
                self.game_over = True
            else:
                print("Invalid choice. Choose again")

    def random_num(self):
        return random.randint(1, 100)

    def get_coin_result(self):
        num = self.random_num()
        coin = ""

        if 1 <= num <= 50:
            coin = "Heads"
        elif 51 <= num <= 100:
            coin = "Tails"

        return coin

    def timer(self):
        total_time = 4
        timer_done = False
        start_time = time.time()

        while not timer_done:
            elapsed_time = time.time() - start_time # Get how much time has passed
            
            if elapsed_time == 1.0:
                print ("3")
            elif elapsed_time == 2.0:
                print ("2")
            elif elapsed_time == 3.0:
                print ("1")
            elif elapsed_time >= total_time:
                start_time = time.time() # Reset timer
                timer_done = True

    def coin_flip(self):
        print("")
        print(f"You will now fight the dragon {self.enemy.name}!")
        print("A coin will now be flipped to determine who goes first!")
        print(f"Heads means you go first. Tails means {self.enemy.name} goes first.")
        print("")
        print("Coin Flipping...")

        coin_result = self.get_coin_result()
        self.timer()
        print(f"The result is: {coin_result}")

        if coin_result == "Heads":
            print("You are attacking first!")
        if coin_result == "Tails":
            print(f"{self.enemy.name} is attacking first!")

    def game_setup(self):
        print("Welcome to Battle Game")

        self.display_options()
        self.make_choice()
        self.coin_flip()

    def play_game(self):
        print("")

def run_game():
    game_obj = Game()
    game_obj.game_setup()

    """
    while not game_over:
        game_obj.play_game()
    """

run_game()
