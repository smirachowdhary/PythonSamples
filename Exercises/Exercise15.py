from sys import argv # imports argv which is a 

script, filename = agrv, argv

txt = open(filename) # opens a file

print(f"Here's your file {filename}:")
print(txt.read()) # prints everything in file

print ("Type the filename again:")
file_again = input)("Enter Here:")

txt_again = open(file_again)# opens a file

print(txt_again.read())# prints everything in file
print("""
    This is stuff I typeed into a file.
    It is really cool stuff.
    Lots and lots of fun to have in here.
""")