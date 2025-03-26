import random
import time

# Implementing and comparing binary search and naive search methods

# Naive search (Linear Search): 
# This method scans the entire list one by one to find the target.
# If found, it returns the index; otherwise, it returns -1.
def naive_search(l, target):
    for i in range(len(l)):  # Loop through the entire list
        if l[i] == target:   # If the target is found
            return i         # Return its index
    return -1  # If not found, return -1


# Binary search (Efficient Search using Divide and Conquer):
# This method works only on sorted lists.
# It repeatedly divides the list into two halves to find the target quickly.
def binary_search(l, target, low=None, high=None):
    if low is None:
        low = 0  # Start from the first index
    if high is None:
        high = len(l) - 1  # End at the last index

    if high < low:  
        return -1  # If the range is invalid, return -1 (not found)

    midpoint = (low + high) // 2  # Find the middle index

    if l[midpoint] == target:  # If the middle element is the target
        return midpoint  # Return its index
    elif target < l[midpoint]:  
        # If target is smaller, search in the left half
        return binary_search(l, target, low, midpoint - 1)
    else:  
        # If target is greater, search in the right half
        return binary_search(l, target, midpoint + 1, high)


if __name__ == '__main__':
    length = 10000  # Define the length of the list

    # Create a sorted list of 10000 unique random numbers
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3 * length, 3 * length))  # Add random numbers
    sorted_list = sorted(list(sorted_list))  # Convert set to sorted list

    # Measure time taken by naive search
    start = time.time()
    for target in sorted_list:
        naive_search(sorted_list, target)  # Search each element using naive search
    end = time.time()
    print("Naive search time: ", (end - start), "seconds")  # Print execution time

    # Measure time taken by binary search
    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)  # Search each element using binary search
    end = time.time()
    print("Binary search time: ", (end - start), "seconds")  # Print execution time
