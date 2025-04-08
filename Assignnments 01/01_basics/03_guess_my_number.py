import random

def main():
    num = random.randint(1, 99)
    print("I am thinking of a number between 1 and 99...")
    
    while True:
        guess = int(input("Enter a guess: "))
        if guess < num:
            print("Your guess is too low\n")
        elif guess > num:
            print("Your guess is too high\n")
        else:
            print(f"Congrats! The number was: {num}")
            break

if __name__ == '__main__':
    main()






# def main():
#     # Randomly do numbers choose karte hain
#     num1 = random.randint(1, 20)
#     num2 = random.randint(1, 10)

#     # Ek random operator choose karte hain
#     operator = random.choice(['+', '-', '*'])
    
#     # Question generate karte hain based on operator
#     if operator == '+':
#         correct_answer = num1 + num2
#         question = f"{num1} + {num2}"
#     elif operator == '-':
#         correct_answer = num1 - num2
#         question = f"{num1} - {num2}"
#     else:
#         correct_answer = num1 * num2
#         question = f"{num1} * {num2}"
    
#     print(f"🧠 Solve this: {question}")

#     attempts = 0  # Kitni baar try kiya

#     while True:
#         try:
#             guess = int(input("Enter your answer: "))
#             attempts += 1

#             if guess < correct_answer:
#                 print("📉 Too low!\n")
#             elif guess > correct_answer:
#                 print("📈 Too high!\n")
#             else:
#                 print(f"🎉 Correct! {question} = {correct_answer}")
#                 print(f"✅ You solved it in {attempts} tries!")
#                 break

#         except ValueError:
#             print("❗Please enter a valid number!\n")

# if __name__ == '__main__':
#     main()
