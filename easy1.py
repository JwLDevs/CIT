# Icecream for everyone

wallet = input("how much euros do you have ")
icecream = input("whats Price of 1 Ice Cream in euros dawg ")

print("Your balance: " + wallet)
if (int(wallet) < int(icecream) * 10):
    print("You don't have enough money, you need" + str(int(wallet) - int(icecream) * 10) )
else:
    print("Your change: " + str(int(wallet) - int(icecream) * 10))