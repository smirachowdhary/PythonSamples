from sys import argv
from os.path import exists
# "c:\smira\github\test.txt", "c:\smira\github\randomfile.txt"
script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}.")

in_file, indata = open(from_file), in_file.read()

print(f"The input file in {len(indata)} bytes long.")

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, it is done.")

out_file.close()
in_file.close()