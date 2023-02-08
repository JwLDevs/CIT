# Lucky number function - Advanced 4

import random

def lucky_number(name, shoe_size, age):
    print("Your luckyy number is: " + str(round(len(name) - shoe_size + age)))

randomName = ["Joe", "Thomas", "Don", "Howard", "Sammy", "Bobson", "Johny", "Edward", "Jenny", "Lily", "Sally", "Samantha"]
randomAge = random.randint(7, 80)
shoeSize = random.randint(6, 12)

lucky_number(randomName[random.randint(0, len(randomName))], int(shoeSize), int(randomAge))