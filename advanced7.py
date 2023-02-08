# BMI-function - Advanced 7

weight = input("Whats yo weight boi (kg) ").replace("kg", "")
height = input("how tall r u dawg (m) ").replace("m", "")

BMI = int(weight) / (float(height) * float(height))

print("Your BMI is: " + str(round(BMI, 3)))

if (int(BMI) > 25):
    print("You are overweight LMAOOO")
elif (int(BMI) < 24.9 and int(BMI) > 18.5):
    print("zamn bru u healthy")
elif (int(BMI) < 18.5):
    print("You are underweight. just like meh")