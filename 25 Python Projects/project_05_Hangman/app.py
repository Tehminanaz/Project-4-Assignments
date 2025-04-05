import random  # Importing the random module to choose a random word

def hangman():
    # List of possible words
    words = ["python", "programming", "hangman", "developer", "computer", "laptop", "science"]
    
    # Randomly select a word from the list
    word = random.choice(words)
    
    # Store unique letters from the word
    word_letters = set(word)
    
    # Set of all alphabets
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    
    # Store letters guessed by the user
    used_letters = set()
    
    # Set number of chances/lives
    lives = 6

    print("\n🎉 Welcome to Hangman! 🎉")

    # Main game loop: runs while the word is not guessed and lives remain
    while len(word_letters) > 0 and lives > 0:
        # Show lives left and used letters
        print("\nYou have", lives, "lives left and you have used these letters:", ' '.join(used_letters))
        
        # Display current progress: guessed letters shown, others as '_'
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print("Current word: ", ' '.join(word_list))

        # Ask user to guess a letter
        user_letter = input("Guess a letter: ").lower()

        # If input is a new valid letter
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)  # Add to used letters
            if user_letter in word_letters:
                word_letters.remove(user_letter)  # Correct guess
                print("✅ Correct guess!")
            else:
                lives -= 1  # Wrong guess, lose a life
                print("❌ Wrong guess! You lost a life.")
        
        # If letter was already guessed
        elif user_letter in used_letters:
            print("⚠️ You already used that letter. Try again.")
        
        # If invalid input (like number or symbol)
        else:
            print("❌ Invalid input. Please enter a letter.")

    # When loop ends, check how the game ended
    if lives == 0:
        print(f"\n💀 You died! The word was '{word}'.")
    else:
        print(f"\n🎉 Congratulations! You guessed the word '{word}' correctly!")

# Start the game
hangman()
