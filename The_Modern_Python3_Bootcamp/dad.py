# Importing the modules
from pyfiglet import figlet_format
from termcolor import colored
from requests import get
from random import choice

# Defining url
url = "https://www.icanhazdadjoke.com/search"

# Welcome screen
print(colored(figlet_format("Dad Joke 3000"), choice(
    ["red", "green", "yellow", "blue", "magenta", "cyan", "white"])))

# Asking for user input
print("Hi! Let me tell you a joke")
user_input = input("What kind of joke do you want? ")

# Searching for the joke
response = get(
    url,
    headers={"Accept": "application/json"},
    params={"term": user_input}
).json()

num_jokes = response["total_jokes"]
# Doing the logic, printing joke
if num_jokes == 0:
    print(f"Sorry, no jokes about {user_input} found. Try again.")
elif num_jokes == 1:
    print(f"I've found one joke about {user_input}. Here it is:")
    print(response["results"][0]["joke"])
else:
    print(
        f"I've found {num_jokes} jokes about {user_input}. Here's one of them:")
    print(choice(response["results"])["joke"])
