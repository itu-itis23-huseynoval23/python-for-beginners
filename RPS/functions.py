import random 

def get_choices():
    #intro to variables
    player_choice = input("Enter a choice (rock, paper, scissors: ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

# choices = get_choices()
# print(choices)

def check_win(player, computer):
    return[player, computer]