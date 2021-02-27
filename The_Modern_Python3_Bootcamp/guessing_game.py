from random import randint

play_again = "y"
while play_again == "y":
    num = randint(1,10)
    guess = None
    while guess != num:
        guess = int(input("What's your guess? "))
        if guess < num:
            print("Too low. Try again.")
        elif guess > num:
            print("Too high. Try again.")
    print("Correct!")
    play_again = input("Do you want to play again? (y/n) ")
