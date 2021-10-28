from cs50 import get_int

# prompt user input
x = get_int('x: ')
y = get_int('y: ')

# perform addition
print(x + y) # This returns the right answer

# if you forget to validate the data, it will just concatenate e.g

x = input("x: ")
y = input("y: ")
print(x + y) # This will return 12 if x = 1 and y = 2 because the input() functions treats everything as a string

# You can fix the above code by parsing int() function around the input e.g

x = int(input('x:'))
y = int(input('y:'))
print(x + y) # This will perform the addition

# Catching errors incase someone enters a word instead of a number
try:
    x = int(input('x: '))
except:
    print("That is not an int!")
    exit()
try:
    y = int(input('y: ')) 
except:
    print("That is not an int!")   
    exit()  
print(x + y)          

# Division of numbers
a = int(input('a:'))
b = int(input('b:'))
z = a / b
print(a / b) # Will have a float
print(a // b) # Will get rid of the float
print(f'{z:.100f}') # Will print out 100 floating digits