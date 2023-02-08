# Password Generator

import random
import string

password_generator = input("Type [y] for a free strong password ")

if (password_generator == "y"):

    letters = string.ascii_letters
    numbers = string.digits
    arr = []

    for i in range(8):
        str(arr.append(random.choice(letters + numbers)))
    
    print('\n\033[1m' + "Your password is: " + '\033[0;0m')
    print("".join(arr))

else:
    print("ok fuck off then")
