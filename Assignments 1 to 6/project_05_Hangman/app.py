import random  # Importing the random module to randomly choose a word

def hangman():
    # List of words to choose from
    words = ["python", "programming", "hangman", "developer", "computer", "laptop", "science"]
    # Randomly select a word from the list
    word = random.choice(words)
    word_letters = set(word)  # Store unique letters in the word
    alphabet = set('abcdefghijklmnopqrstuvwxyz')  # The entire alphabet
    used_letters = set()  # Set to keep track of used letters by the player

    lives = 6  # The number of lives the player has

    print("\n🎉 Welcome to Hangman! 🎉")

    # Main game loop
    while len(word_letters) > 0 and lives > 0:
        # Show how many lives are left and the letters the player has guessed
        print("\nYou have", lives, "lives left and you have used these letters:", ' '.join(used_letters))

        # Display the word with underscores for unguessed letters
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print("Current word: ", ' '.join(word_list))

        # Ask the player to guess a letter
        user_letter = input("Guess a letter: ").lower()

        # Check if the letter is a valid input and not already used
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)  # Correct guess: remove the letter from word_letters
                print("✅ Correct guess!")
            else:
                lives -= 1  # Incorrect guess: reduce lives
                print("❌ Wrong guess! You lost a life.")
        elif user_letter in used_letters:
            print("⚠️ You already used that letter. Try again.")
        else:
            print("❌ Invalid input. Please enter a letter.")

    # End of the game
    if lives == 0:
        print(f"\n💀 You died! The word was '{word}'.")
    else:
        print(f"\n🎉 Congratulations! You guessed the word '{word}' correctly!")

# Start the game
hangman()
