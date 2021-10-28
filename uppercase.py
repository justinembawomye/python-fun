from cs50 import get_string

before = get_string('Before: ').upper()
print("After: ", end="")
for a in before:
    print(a, end="")

print()    