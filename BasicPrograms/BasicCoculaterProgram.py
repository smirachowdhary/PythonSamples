TypeOfArthematic = input("Enter type of arthematic (a, s, m, d, and p):")

n1 = float(input("Enter 1st number in calculation:"))
n2 = float(input("Enter 2st number in calculation:"))

if TypeOfArthematic == "m":
    print(f"The answer to your math problem is {n1*n2}.")
elif TypeOfArthematic == "a":
    print(f"The answer to your math problem is {n1+n2}.")
elif TypeOfArthematic == "s":
        print(f"The answer to your math problem is {n1-n2}.")
elif TypeOfArthematic == "d":
        if n2 == 0:
            print("You cannot divide a number by 0.")
        else:
            print(f"The answer to your math problem is {n1//n2}.")
            print (f"The complete d is {n1/n2}.")
            if n1 % n2 > 0:
                print(f"The remainder is {n1%n2}.")
elif TypeOfArthematic == "p":
    print(f"The answer to {n1} to the p of {n2} is {n1**n2}.")