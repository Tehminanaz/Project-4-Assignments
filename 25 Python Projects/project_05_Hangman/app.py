import random

def hangman():
    words = ["python", "programming", "hangman", "developer", "computer", "laptop", "science"]
    word = random.choice(words)  # Randomly select a word
    word_letters = set(word)  # Unique letters in the word
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    used_letters = set()  # What the player has guessed

    lives = 6  # Number of tries

    print("\n🎉 Welcome to Hangman! 🎉")

    # Main loop
    while len(word_letters) > 0 and lives > 0:
        # Show current state
        print("\nYou have", lives, "lives left and you have used these letters:", ' '.join(used_letters))
        
        # Display current word with underscores
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print("Current word: ", ' '.join(word_list))

        # Get user input
        user_letter = input("Guess a letter: ").lower()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print("✅ Correct guess!")
            else:
                lives -= 1
                print("❌ Wrong guess! You lost a life.")
        elif user_letter in used_letters:
            print("⚠️ You already used that letter. Try again.")
        else:
            print("❌ Invalid input. Please enter a letter.")

    # Game over
    if lives == 0:
        print(f"\n💀 You died! The word was '{word}'.")
    else:
        print(f"\n🎉 Congratulations! You guessed the word '{word}' correctly!")

# Start the game
hangman()
