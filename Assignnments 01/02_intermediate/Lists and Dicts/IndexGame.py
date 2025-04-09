# Function to access an element at a specific index in the list
def access_element(lst, index):
    try:
        # Try to return the element at the specified index
        return lst[index]
    except IndexError:
        # If index is out of range, return an error message
        return "Index out of range."

# Function to modify an element at a specific index in the list
def modify_element(lst, index, new_value):
    try:
        # Try to modify the element at the specified index
        lst[index] = new_value
        return lst  # Return the updated list
    except IndexError:
        # If index is out of range, return an error message
        return "Index out of range."

# Function to slice a list from the start index to the end index (not including the end index)
def slice_list(lst, start, end):
    # Slicing won't raise an IndexError, just return the sliced part of the list
    return lst[start:end]

# Main function for the game-like operation
def index_game():
    # Example list
    lst = [1, 2, 3, 4, 5]  
    print("Current list:", lst)  # Show the current list
    
    # Ask the user what operation they want to perform
    print("Choose an operation: access, modify, slice")
    operation = input("Enter operation: ").lower()

    # Perform the corresponding operation based on user input
    if operation == "access":
        # Ask for the index to access an element
        index = int(input("Enter index to access: "))
        print("Result:", access_element(lst, index))  # Call access function and print result
    elif operation == "modify":
        # Ask for the index and the new value to modify
        index = int(input("Enter index to modify: "))
        new_value = input("Enter new value: ")
        print("Updated List:", modify_element(lst, index, new_value))  # Call modify function and print updated list
    elif operation == "slice":
        # Ask for the start and end index for slicing the list
        start = int(input("Enter start index: "))
        end = int(input("Enter end index: "))
        print("Sliced List:", slice_list(lst, start, end))  # Call slice function and print sliced list
    else:
        print("Invalid operation.")  # If operation is not valid

# Run the game when the script is executed
if __name__ == '__main__':
    index_game()
