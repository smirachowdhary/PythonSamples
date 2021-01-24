from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit Crtl + C(^C)")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, "w")

print("Truncating the file. Goodbye.")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("Line 1:")
line2 = input("Line 2:")
line3 = input("Line 3:")

print("I am going to write these to the file.")

target.write(f" {line1} \n {line2} \n {line3} \n")

print("And fianally, we close it.")
target.close()