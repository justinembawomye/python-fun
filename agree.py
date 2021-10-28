from cs50 import get_string

s = get_string('Do you agree?')

s = s.lower() # This will convert whatever value assigned to s to lower case

# Works, but does not send a response when one uses capital letters or when you add something that is not in that range
if s in ['y', 'yes']:
    print('Agreed')
elif s in ['n', 'no']:
    print('Not agreed')

# Solution. Force everything to lower case
if s.lower() in ['y', 'yes']:
    print('Agreed')
elif s.lower() in ['n', 'no']:
    print('Not agreed')



