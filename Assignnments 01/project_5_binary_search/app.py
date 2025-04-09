# Importing necessary modules
import random           # For generating random numbers
import time             # For measuring execution time
from bisect import bisect_left  # For using Python's built-in binary search

# --------- Binary Search Python Project ---------
# This project shows three ways to search in a list:
# 1. Naive (simple linear) search
# 2. Recursive binary search
# 3. Built-in bisect search
# It also includes performance comparison and user input to test them.

# Naive Search: checks each item in the list one by one
def naive_search(lst, target):
    """Naive search scans the entire list for the target."""
    for i, item in enumerate(lst):  # Loop through the list
        if item == target:
            return i  # Return the index if found
    return -1  # Return -1 if not found

# Recursive Binary Search: works only on sorted lists
def binary_search(lst, target, low=0, high=None):
    """Recursive binary search on a sorted list."""
    if high is None:
        high = len(lst) - 1

    if high < low:
        return -1  # Base case: target not found

    midpoint = (low + high) // 2

    if lst[midpoint] == target:
        return midpoint  # Found at the midpoint
    elif target < lst[midpoint]:
        return binary_search(lst, target, low, midpoint - 1)  # Search in the left half
    else:
        return binary_search(lst, target, midpoint + 1, high)  # Search in the right half

# Built-in Bisect Search: uses Python's built-in module
def builtin_bisect_search(lst, target):
    """Uses Python's bisect module for binary search."""
    index = bisect_left(lst, target)  # Finds the index where target should be
    if index != len(lst) and lst[index] == target:
        return index  # Found the target
    return -1  # Not found

# Function to test how fast each method works
def performance_test():
    length = 10000  # Length of the list
    sorted_list = sorted(random.sample(range(-3 * length, 3 * length), length))  # Generate random sorted list

    # Measure time for naive search
    start = time.perf_counter()
    for target in sorted_list:
        naive_search(sorted_list, target)
    print(f"Naive search time: {time.perf_counter() - start:.4f} seconds")

    # Measure time for recursive binary search
    start = time.perf_counter()
    for target in sorted_list:
        binary_search(sorted_list, target)
    print(f"Recursive binary search time: {time.perf_counter() - start:.4f} seconds")

    # Measure time for built-in bisect search
    start = time.perf_counter()
    for target in sorted_list:
        builtin_bisect_search(sorted_list, target)
    print(f"Built-in bisect search time: {time.perf_counter() - start:.4f} seconds")

# Function to take user input and test search methods
def user_search():
    """Allow user to enter a target number and choose search method."""
    lst = sorted(random.sample(range(-1000, 1000), 100))  # Generate a small sorted list
    print("\nGenerated sorted list:")
    print(lst)

    # Get a valid integer input from the user
    while True:
        user_input = input("\nEnter a number to search: ")
        try:
            target = int(user_input)
            break
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

    # Ask the user to choose a search method
    print("Choose a search method:")
    print("1. naive")
    print("2. binary")
    print("3. bisect")

    # Map input to method names
    method_map = {"1": "naive", "2": "binary", "3": "bisect", "naive": "naive", "binary": "binary", "bisect": "bisect"}

    # Get a valid method choice
    while True:
        method_input = input("Enter method name or number: ").strip().lower()
        method = method_map.get(method_input)
        if method:
            break
        else:
            print("Invalid method! Please enter '1', '2', '3' or method names (naive, binary, bisect).")

    # Call the selected search method
    if method == 'naive':
        result = naive_search(lst, target)
    elif method == 'binary':
        result = binary_search(lst, target)
    else:
        result = builtin_bisect_search(lst, target)

    # Show result to the user
    if result != -1:
        print(f"Target found at index {result}.")
    else:
        print("Target not found.")

# Run the performance test and user search when the script runs
if __name__ == "__main__":
    print("\n---- Performance Test ----")
    performance_test()

    print("\n---- User Search ----")
    user_search()
