# Making a rock, paper, scissors game

# Importing sys module (for exit())
from sys import exit

# Welcome screen:
print("Welcome to the game rock, paper, scissors!")
print("***Rock***")
print("***Paper***")
print("***Scissors***")

# Player1's choice
player1 = input("Player 1, what do you choose? (rock/paper/scissors) ")
if not player1:
    print("You didn't enter anything")
    exit()
# NO CHEATING!
print("-------------NO CHEATING!-------------\n\n" * 20)
# Player2's choice
player2 = input("Player 2, what do you choose? (rock/paper/scissors) ")
if not player2:
    print("You didn't enter anything")
    exit()
# SHOOT!
print("SHOOT!")

# The logic
if player1 == player2:
    print("Tie!")
elif player1 == "rock":
    if player2 == "paper":
        print("Player 2 wins!")
    elif player2 == "scissors":
        print("Player 1 wins!")
elif player1 == "paper":
    if player2 == "rock":
        print("Player 1 wins!")
    elif player2 == "scissors":
        print("Player 2 wins!")
elif player1 == "scissors":
    if player2 == "rock":
        print("Player 2 wins!")
    elif player2 == "paper":
        print("Player 1 wins!")
else:
    print("Something went wrong . . .")

# Bye-bye screen
print("Thanks for playing!")