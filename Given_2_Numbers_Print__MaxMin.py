a = int(input("Enter number:"))
b = int(input("Enter number:"))

if a > b:
    print (f"""{a} is max of {a} and {b}.
    {b} is min of {a} and {b}.""")
elif b > a:
    print (f"""{b} is max of {a} and {b}.
    {a} is min of {a} and {b}.""")
else:
    print (f" {a} is equal to {b}.")