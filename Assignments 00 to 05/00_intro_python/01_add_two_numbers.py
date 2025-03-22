def main():
    print("This program adds two numbers.")
    
    # 1 Prompt of the user and convert it to an integer
    num1 = int(input("Enter first number: "))
    
    # 2 Prompt of the user and convert it to an integer
    num2 = int(input("Enter second number: "))
    
    # Calculate the sum
    total = num1 + num2
    
    #  result
    print("The total is " + str(total) + ".")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
