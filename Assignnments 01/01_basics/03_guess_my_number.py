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
