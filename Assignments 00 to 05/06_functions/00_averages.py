
# Problem Statement
# Write a function that takes two numbers and finds the average between the two.

def average(a:float, b:float):
    return (a + b) / 2

def main():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print(f"The average of {num1} and {num2} is {average(num1, num2)}")

if __name__ == '__main__':
    main()