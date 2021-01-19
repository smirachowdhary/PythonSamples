FOI = input("Are you going to do fraction and decimal arthematic or whole and negative numbers arthematic?")

if FOI == "whole and negative numbers":
    TypeOfArthematic = input("Enter type of arthematic (addition, subtraction, multiplacation, division, and power):")

    n1 = int(input("Enter 1st number in calculation:"))
    n2 = int(input("Enter 2st number in calculation:"))

    if TypeOfArthematic == "multiplacation":
        print(f"The answer to your math problem is {n1*n2}.")
    elif TypeOfArthematic == "addition":
        print(f"The answer to your math problem is {n1+n2}.")
    elif TypeOfArthematic == "subtraction":
            print(f"The answer to your math problem is {n1-n2}.")
    elif TypeOfArthematic == "division":
            if n2 == 0:
                print("You cannot divide a number by 0.")
            else:
                print(f"The answer to your math problem is {n1//n2}.")
                print (f"The complete division is {n1/n2}.")
                if n1 % n2 > 0:
                    print(f"The remainder is {n1%n2}.")
    elif TypeOfArthematic == "power":
        print(f"The answer to {n1} to the power of {n2} is {n1**n2}.")
else:
    TypeOfArthematic = input("Enter type of arthematic (addition, subtraction, multiplacation, division, and power):")

    n1 = float(input("Enter 1st number in calculation:"))
    n2 = float(input("Enter 2st number in calculation:"))

    if TypeOfArthematic == "multiplacation":
        print(f"The answer to your math problem is {n1*n2}.")
    elif TypeOfArthematic == "addition":
        print(f"The answer to your math problem is {n1+n2}.")
    elif TypeOfArthematic == "subtraction":
            print(f"The answer to your math problem is {n1-n2}.")
    elif TypeOfArthematic == "division":
            if n2 == 0:
                print("You cannot divide a number by 0.")
            else:
                print(f"The answer to your math problem is {n1//n2}.")
                print (f"The complete division is {n1/n2}.")
                if n1 % n2 > 0:
                    print(f"The remainder is {n1%n2}.")
    elif TypeOfArthematic == "power":
        print(f"The answer to {n1} to the power of {n2} is {n1**n2}.")