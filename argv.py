# Commandline Arguements
from sys import argv

if len(argv) == 2:
    print(f"Hello, {argv[1]}")
else:
    print("Hello world!")    

# for loop to print out arguments incase they are provided
for a in argv:
    print(a)    

# Slicing the argv.py filename
for i in argv[1:]:
    print(i)