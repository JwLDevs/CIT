# Pay counter

income = input("What is your gross income? (MYR) ")

print("\n--------------------")
print('\033[1m' + "Tax rate: " + "\033[0;0m" + str(round(int(income) * 0.24, 2)))
print('\033[1m' + "Pesion contribution: " + "\033[0;0m" + str(round(int(income) * 0.06, 2)))
print('\033[1m' + "Unemployment insurance free: " + "\033[0;0m" + str(round(int(income) * 0.02, 2)))
print('\033[1m' + "Net income: " + "\033[0;0m" + str(round(int(income) - int(income) * 0.32, 2)))
print("--------------------")