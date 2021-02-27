# Making a rock, paper, scissors game where the player competes against a computer.
# Importing random and sys module
from random import choice
from sys import exit

# Welcome screen
print("Welcome to the rock, paper, scissors game!")
print("This RPS is unique! How? Well, you're playing against the DUMBEST AI IN THE WORLD!")
print("***Rock***")
print("***Paper***")
print("***Scissors***")

# Player & computer make the choice . . .
player = input("So, what do you choose? ").lower()
if not player:
    print("You didn't enter ANYTHING! How dare you?!?!")
    exit()
computer = choice(["rock","paper","scissors"])
print(f"And the computer made his choice: {computer}!")

# The logic
if player == computer:
    print("TIE!")
elif player == "rock":
    if computer == "paper":
        print("The computer wins *sighs*")
    else:
        print("YOU WIN!!!!!!")
elif player == "paper":
    if computer == "rock":
        print("YOU WIN!!!!!!")
    else:
        print("The computer wins *sighs*")
elif player == "scissors":
    if computer == "rock":
        print("The computer wins *sighs*")
    else:
        print("YOU WIN!!!!!!")
else:
    print("Something went wrong . . .")

# Bye screen
print("Thanks for playing!")