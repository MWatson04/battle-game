# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

import time
import random
from character import *
from sys import exit

class Game:
    def __init__(self, enemy = Dragon()):
        self.game_over = False
        self.chosen_class = None
        self.enemy = enemy
        self.attack_first = None
        self.winner = None

    def display_options(self):
        print("Welcome to Battle Game")
        print("")
        print("Please select your class to start")
        print("1)   Human")
        print("2)   Elf")
        print("3)   Orc")
        print("4)   Wizard")
        print("5)   Exit")

    def make_choice(self):
        valid_choice = False
    
        while not valid_choice:
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
            elif class_input in ("5", "exit"):
                print("")
                print("Goodbye!")
                exit()
            else:
                print("Invalid choice. Choose again")

    def get_coin_result(self):
        num = random.randint(1, 100)
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
        print("(You get to go twice in a row if the coin lands in your favor)")
        print("")
        print("Coin Flipping...")

        coin_result = self.get_coin_result()
        self.timer()
        print(f"The result is: {coin_result}")

        if coin_result == "Heads":
            print("You are attacking first!")
            print("")
            self.attack_first = "player"
        if coin_result == "Tails":
            print(f"{self.enemy.name} is attacking first!")
            print("")
            self.attack_first = "enemy"

    def game_setup(self):
        self.display_options()
        self.make_choice()
        self.coin_flip()

    def enemy_turn(self):
        print(f"{self.enemy.name} is attacking!")
        self.enemy.attack()
        self.chosen_class.take_damage(self.enemy.damage)

    def player_turn(self):
        valid_choice = False

        while not valid_choice:
            player_attack = input("Type 'attack' to perform your attack: ").lower()

            if player_attack == "attack":
                self.chosen_class.attack()
                self.enemy.take_damage(self.chosen_class.damage)
                valid_choice = True
            else:
                print("Invalid choice. Try again.")
 
    def play_game(self):
        if self.attack_first == "player":
            self.player_turn()
        elif self.attack_first == "enemy":
            self.enemy_turn()

        while not self.game_over:       
            self.player_turn()
            if self.enemy.health <= 0:
                self.winner = "player"
            if self.winner == "player":
                print("You WIN!")
                self.game_over = True
                break
            
            self.enemy_turn()
            if self.chosen_class.health <= 0:
                self.winner = "enemy"
            if self.winner == "enemy":
                print("You LOSE")
                self.game_over = True
                break  
