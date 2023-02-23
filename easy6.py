# Calculator

def calculation():    

    global calculator
    calculator = input("Ask a question uwu ").replace("+", " + ").replace("-", " - ").replace("*", " * ").replace("/", " / ").replace("x", " * ")

    global question
    question = calculator.split(" ")
    #print(question)

    work_out = "".join(question)

    if ("+" in question):
        print(str(work_out) + " = " + str(int(question[0]) + int(question[len(question) - 1])))

    elif ("-" in question):
        print(str(work_out) + " = " + str(int(question[0]) - int(question[len(question) - 1])))
    
    elif ("*" in question):
        print(str(work_out) + " = " + str(int(question[0]) * int(question[len(question) - 1])))

    elif ("/" in question):
        print(str(work_out) + " = " + str(int(question[0]) / int(question[len(question) - 1])))
        
    else:
        print("Invalid syntax.")


while True:
    calculation()
    if (calculator == "quit"):
        break