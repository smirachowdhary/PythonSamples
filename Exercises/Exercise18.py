def print_three(*args):
    arg1, arg2, arg3 = args
    print(f"arg1: {arg1} arg2: {arg2} arg3: {arg3}")

def print_two(arg1, arg2):
    print(f"arg1: {arg1} arg2: {arg2}")

def print_one(arg1):
    print(f"arg1: {arg1}")

def print_none():
    print("I've got nothin'.")

print_three("Smira", "V.", "Chowdhary")
print_two("Smira V.", "Chowdhary")
print_one("Smira V. Chowdhary")
print_none()