# Rap name generator - Advanced 3
import string
import random

first_name = input("What is your first name? ")
random_first_letter = random.choice(string.ascii_letters)
random_prefix = ["Lil", "Dj"]


print("\nHmm.. how about " + '\033[1m' +  random.choice(random_prefix) + " " + first_name.replace(first_name[0], random_first_letter.upper()) + '\033[0;0m' + "?")
