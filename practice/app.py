# import random

# def main():
#     num1 = int(input("write the first number: "))
#     num2 = int(input("write the second number: "))

#     total = num1 + num2

#     print(f"this is a sum of your number {total}")

# if __name__ == "__main__":
#     main()

# def main():

#     animal1 = input("what's your favorite animal: ")

#     print(f"My favorite animal is also {animal1}")

# if __name__ == "__main__":
#     main()

# def main():
#     # Prompt the user for temperature in Fahrenheit
#     degrees_fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    
#     # Convert Fahrenheit to Celsius
#     degrees_celsius = (degrees_fahrenheit - 32) * 5.0 / 9.0
    
#     # Display the result
#     print("Temperature: " + str(degrees_fahrenheit) + "F = " + str(degrees_celsius) + "C")

# # This provided line is required at the end of
# # Python file to call the main() function.
# if __name__ == '__main__':
#     main()

# def main():
#     anton = 21  # Anton's age is 21
#     beth = anton + 6  # Beth is 6 years older than Anton
#     chen = beth + 20  # Chen is 20 years older than Beth
#     drew = chen + anton  # Drew is Chen's age plus Anton's age
#     ethan = chen  # Ethan is the same age as Chen

#     # Printing their names and ages
#     print("Anton is " + str(anton))
#     print("Beth is " + str(beth))
#     print("Chen is " + str(chen))
#     print("Drew is " + str(drew))
#     print("Ethan is " + str(ethan))

# # This provided line is required at the end of
# # Python file to call the main() function.
# if __name__ == '__main__':
#     main()


# def main():
#     # Prompt the user for the lengths of each side
#     side1 = float(input("What is the length of side 1? "))
#     side2 = float(input("What is the length of side 2? "))
#     side3 = float(input("What is the length of side 3? "))

#     # Calculate the perimeter
#     perimeter = side1 + side2 + side3

#     # Output the result
#     print("The perimeter of the triangle is " + str(perimeter))

# # This provided line is required at the end of
# # Python file to call the main() function.
# if __name__ == '__main__':
#     main()


# prompt = "what i do"
# joke = "hahahaha"
# sorry = "i am sorry try again"

# def main():

#     user_input = input(prompt)

#     if user_input == "joke":
#         print(joke)
#     else:
#         print(sorry)

# if __name__ == "__main__":
#     main()

# prompt = "what you want"
# joke = "here is a jooke for yoy hahahhaha"
# sorry = "sorry i only tell a joke"

# def main():

#     user_input = input(f"{prompt}: ")

#     if "joke" in user_input:
#         print(joke)
#     else:
#         print(sorry)

# if __name__ == "__main__":
#     main()



# def main():
#     curr_value = int(input("Enter a number: "))

#     while curr_value < 100:
#         curr_value = curr_value * 2
#         print(curr_value)

# if __name__ == '__main__':
#     main()




# def main():
#     curr_value = int(input("write a number: "))

#     while curr_value < 100:

#         curr_value = curr_value * 2
#         print(curr_value)

# if __name__ == "__main__":
#     main()

# def main():
#     for i in range(10, 0, -1):
#         print(i)
#     print("Liftoff!")

# if __name__ == '__main__':
#     main()

# def main():
#     for i in range(10,0, -1):
#         print(i)
#     print("Lift off")

# if __name__ == "__main__":
#     main()


# def guees_game(x):

#     random_number = random.randint(1, x)
#     guess = 0

#     while guess != random_number:

#         guess = int(input(f"Guess the number between 1 and {x} : "))

#         if guess < random_number:
#             print("its to low")
#         elif guess > random_number:
#             print("its to high")

#     print("yay congratulation!")

# guees_game(10)

# def guess_game(x):

#     random_number = random.randint(1, x)
#     guess = 0

#     while guess != random_number:

#         guess = int(input(f"Guess the number between 1 and {x} : "))

#         if guess < random_number:
#             print("Its to low")
#         elif guess > random_number:
#             print("Its to high")

#     print("Yay congrtulation!")

# guess_game(10)
        
# import random

# N_NUMBERS = 10
# MIN_VALUE = 1
# MAX_VALUE = 100

# def main():
#     for i in range(N_NUMBERS):
#         print(random.randint(MIN_VALUE, MAX_VALUE), end=" ")

# if __name__ == '__main__':
#     main()









