# Calculator

def calculation():    

    global calculator
    calculator = input("Ask a question uwu ").replace("+", " + ").replace("-", " - ").replace("*", " * ").replace("/", " / ").replace("x", " * ")

    global question
    question = calculator.split(" ")
    print(question)

    if ("+" in question):
        print(int(question[0]) + int(question[len(question) - 1]))

    elif ("-" in question):
        print(int(question[0]) - int(question[len(question) - 1]))
    
    elif ("*" in question):
        print(int(question[0]) * int(question[len(question) - 1]))

    elif ("/" in question):
        print(int(question[0]) / int(question[len(question) - 1]))


while True:
    calculation()
    if (calculator == "quit"):
        break