import random  # Importing the random module to generate random choices

print('Welcome To Password Generator!')  # Welcome message for the user

# Define character set for password generation
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()'  # All possible characters to choose from

# Get user input
number = int(input('Amount of passwords to generate: '))  # Number of passwords to generate
length = int(input('Input your password length: '))  # Desired length of each password

print('\nHere are your passwords:')  # Message to indicate the start of password display

# Generate passwords
for _ in range(number):  # Loop for generating the specified number of passwords
    password = ''.join(random.choice(chars) for _ in range(length))  # Generate a random password by choosing random characters
    print(password)  # Print the generated password
