n = int(input("Enter number here:"))

def get_all_factors(number):
    factors = ""

    for i in range(1,number+1):
        if number % i == 0:
            factor_input = f"{i} "
            factors += factor_input

    return factors

get_all_factors(n)