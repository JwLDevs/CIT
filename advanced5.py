# Name generator - Advanced 5

import random

name = input("Type [y] for a random full name my dei ")

list_first_name = ["Ann", "Matt", "Daniel"]
list_family_name_start = ["Green", "Wein", "Good"]
list_family_name_end = ["smith", "son", "berg"]

if (name == "y"):
    print(str(random.choice(list_first_name) + " " + random.choice(list_family_name_start)) + random.choice(list_family_name_end))
else:
    print("ok didnt ask ratio + bozo L ")