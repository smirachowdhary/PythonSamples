n1 = int(input("Enter number here:"))
n2 = int(input("Enter number here:"))
GCF = ""
smallest_number = ""
biggest_number = ""

if n1 > n2:
    smallest_number = n2
    biggest_number = n1
if n1 < n2:
    smallest_number = n1
    biggest_number = n2
if n1 == n2:
    smallest_number = n1
    biggest_number = n2

for i in range(smallest_number+1,0,-1):
    if smallest_number % i == 0:
        factor = i
        if biggest_number % factor == 0:
            GCD = factor
            break

print(f"GCF is equal to {GCF}")