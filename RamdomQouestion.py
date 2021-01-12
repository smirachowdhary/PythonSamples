import random

n1 = random.randint(1,20)
n2 = random.randint(100,1000)

print (f"{n1} * {n2}")
answer = int(input(""))

if n1 * n2 == answer:
    print ("Great Job! Your answer is correct.")
else:
    print(f"Sorry, you answer is not correct. The real answer is {n1 * n2}.")

n2 = random.randint(1,20)
n1 = random.randint(100,1000)

print (f"{n1} / {n2}")
answer = int(input(""))

if n1 / n2 == answer:
    print ("Great Job! Your answer is correct.")
else:
    print(f"Sorry, you answer is not correct. The real answer is {n1 / n2}.")