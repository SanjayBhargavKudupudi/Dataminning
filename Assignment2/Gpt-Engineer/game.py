import random

class Player:
    def get_choice(self):
        choice = input("Enter your choice (rock, paper, scissors): ")
        return choice
#create a unit test for the player class
class TestPlayer:
    def test_get_choice(self):
        player = Player()
        choice = player.get_choice()
        assert choice in ["rock", "paper", "scissors"]

#refactor code to make it more readable

class Player:
    def get_choice(self):
        choices = ["rock", "paper", "scissors"]
        choice_number = int(input("Enter your choice (0 for rock, 1 for paper, 2 for scissors): "))
        return choices[choice_number]
    
class TestPlayer:
    def test_get_choice(self):
        player = Player()
        choice = player.get_choice()
        assert choice in ["rock", "paper", "scissors"]




class Computer:
    
    def get_choice(self):
        choices = ["rock", "paper", "scissors"]
        return random.choice(choices)

class Game:
    def __init__(self):
        self.player = Player()
        self.computer = Computer()

    def start(self):
        player_choice = self.player.get_choice()
        computer_choice = self.computer.get_choice()

        print(f"You chose {player_choice}, computer chose {computer_choice}.")

        if player_choice == computer_choice:
            print("It's a draw!")
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "scissors" and computer_choice == "paper") or \
             (player_choice == "paper" and computer_choice == "rock"):
            print("You win!")
        else:
            print("You lose!")

if __name__ == "__main__":
    game = Game()
    game.start()
