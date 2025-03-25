import random

print('Welcome To Password Generator!')

# Define character set for password generation
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()'

# Get user input
number = int(input('Amount of passwords to generate: '))
length = int(input('Input your password length: '))

print('\nHere are your passwords:')

# Generate passwords
for _ in range(number):
    password = ''.join(random.choice(chars) for _ in range(length))
    print(password)