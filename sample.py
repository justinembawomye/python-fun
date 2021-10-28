def main():
    height = get_height()
    for i in range(height):
        print('#')

# Try a Do while loop such that the program doesn't break incase of a user puts in wrong values

def get_height():
    while True:
        try:
            n = int(input('Height: '))
            if n > 0:
                break
        except ValueError:
            print("It's not an integer!")
    return n
main()        
        
    #The above function will keep prompting for user input 
