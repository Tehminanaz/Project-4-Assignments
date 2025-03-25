# Write a program which continuously asks the user to enter values which are added one by one into a list. When the user presses enter without typing anything, print the list.

# Here's a sample run (user input is in blue):

# Enter a value: 1 Enter a value: 2 Enter a value: 3 Enter a value: Here's the list: ['1', '2', '3']

def main():
    lst = []  # Create an empty list to store user input

    val = input("Enter a value: ")  # Get the first value from the user
    while val:  # Continue looping until the user presses enter without typing anything
        lst.append(val)  # Add the entered value to the list
        val = input("Enter a value: ")  # Prompt for the next value

    print("Here's the list:", lst)  # Print the complete list after the loop ends


# This line ensures the main function runs when the script is executed
if __name__ == '__main__':
    main()
