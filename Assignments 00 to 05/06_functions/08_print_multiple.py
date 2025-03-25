# Problem Statement
# Fill out print_multiple(message, repeats), which takes as parameters a string message to print, and an integer repeats number of times to print message. We've written the main() function for you, which prompts the user for a message and a number of repeats.

# Here's a sample run of the program (user input is in blue):

# Please type a message: Hello! Enter a number of times to repeat your message: 6 Hello! Hello! Hello! Hello! Hello! Hello!
def main():
    user = input("Please type a message: ")
    multiply = input(f"{user}! Enter a number of times to repeat your message:")

    for i in range(int(multiply)):
        print(user)


if __name__ == '__main__':
    main()