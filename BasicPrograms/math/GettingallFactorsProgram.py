n = int(input("Enter number here:"))
factors = ""

for i in range(1,n+1):
    if n % i == 0:
        factor_input = f"{i} "
        factors += factor_input


print(factors)