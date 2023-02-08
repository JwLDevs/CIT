# Automatic text for lottery

import datetime

firstname = input("Enter your first name: ")
surname = input("Enter your surname: ")

print('\n"Hello ' + firstname + "! \nThank you for participating. Unfortunately, this time you didn't win. \nHowever we can offer you the top prize for only 199 €. Use the following code to purchase:\n THANKS_" + surname.upper() + "\n\nBest wishes\nJames Byte\nMobiles " + str(datetime.date.year))