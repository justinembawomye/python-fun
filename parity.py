# parity of a number: Checks to see if a number is even or odd

from cs50 import get_int
n = get_int("Enter any number")

if n % 2 == 0:
    print("The number is even")
else:
    print("It's an odd number ")    

