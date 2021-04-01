import requests
from bs4 import BeautifulSoup
from random import choice
from pyfiglet import figlet_format
from termcolor import colored

# Welcome screen
print(colored(figlet_format("Quote Guessing Game"), choice(
    ["red", "green", "yellow", "blue", "magenta", "cyan", "white"])))
