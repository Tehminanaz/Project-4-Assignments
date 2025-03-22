def main():
    # Create a list called fruit_list that contains the following fruits:
    fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']

    # Print the length of the list.
    print("Length of the list:", len(fruit_list))

    # Add 'mango' at the end of the list.
    fruit_list.append('mango')

    # Print the updated list.
    print("Updated list:")
    for fruit in fruit_list:
        print(fruit)

if __name__ == '__main__':
    main()
