# Password Generator

import random
import string

password_generator = input("Type [y] for a free strong password ")

if (password_generator == "y"):

    def randomPW():
        letters = string.ascii_letters
        numbers = string.digits

        return ''.join(random.choice(letters + numbers) for i in range(8))
    
    print("Your password: " + randomPW())

else:
    print("ok fuck off then")
