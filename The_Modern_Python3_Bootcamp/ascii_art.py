from pyfiglet import figlet_format
from termcolor import colored

text = input("What message would you like to print? ")
color = input("What color? ")

try:
    result = colored(figlet_format(text), color)
except KeyError:
    result = colored(figlet_format(text), color = "magenta")
print(result)