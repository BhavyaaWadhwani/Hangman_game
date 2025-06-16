import random


def get_random_word_and_hint():
    """
    Selects a random word and its corresponding hint from a predefined list.
    """
    word_data = [
        {"word": "python", "hint": "Programming Language"},
        {"word": "computer", "hint": "Electronic Device"},
        {"word": "developer", "hint": "Occupation"},
        {"word": "algorithm", "hint": "Mathematical/Computer Concept"},
        {"word": "keyboard", "hint": "Computer Hardware"},
        {"word": "monitor", "hint": "Computer Hardware"},
        {"word": "application", "hint": "Software Type"},
        {"word": "internet", "hint": "Global Network"},
        {"word": "website", "hint": "Web Content"},
        {"word": "openai", "hint": "AI Research Company"},
        {"word": "language", "hint": "Communication System"},
        {"word": "machine", "hint": "Mechanical Device"},
        {"word": "learning", "hint": "Cognitive Process"},
        {"word": "artificial", "hint": "Not Natural"},
        {"word": "intelligence", "hint": "Mental Capacity"},
        {"word": "network", "hint": "Interconnected System"},
        {"word": "database", "hint": "Data Storage"},
        {"word": "security", "hint": "Protection/Safety"},
        {"word": "framework", "hint": "Software Structure"}
    ]
    chosen_data = random.choice(word_data)
    return chosen_data["word"].upper(), chosen_data["hint"]


def display_hangman(incorrect_guesses):
    """
    Displays the hangman ASCII art based on the number of incorrect guesses.
    """
    stages = [
        # Stage 0: Initial empty gallows
        """
           -----
           |   |
               |
               |
               |
               |
         -------
        """,
        # Stage 1: Head
        """
           -----
           |   |
           O   |
               |
               |
               |
         -------
        """,
        # Stage 2: Body
        """
           -----
           |   |
           O   |
           |   |
               |
               |
         -------
        """,
        # Stage 3: One arm
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
         -------
        """,
        # Stage 4: Both arms
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
         -------
        """,
        # Stage 5: One leg
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
         -------
        """,
        # Stage 6: Both legs (game over)
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
         -------
        """
    ]
    print(stages[incorrect_guesses])


def display_word_state(word, guessed_letters):
    """
    Displays the current state of the word, showing guessed letters
    and underscores for unguessed ones.
    """
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()


def hangman():
    """
    The main function to run the Hangman game.
    """
    print("Welcome to Hangman!")

    word_to_guess, hint = get_random_word_and_hint()
    guessed_letters = set()
    incorrect_guesses = 0
    guess_limit = 6  # The maximum number of incorrect guesses allowed

    while incorrect_guesses < guess_limit:
        print("\n" + "=" * 30)
        display_hangman(incorrect_guesses)
        print(f"Hint: {hint}")  # Display the hint
        print(f"Word: {display_word_state(word_to_guess, guessed_letters)}")
        print(f"Incorrect guesses remaining: {guess_limit - incorrect_guesses}")
        print(f"Guessed letters: {', '.join(sorted(list(guessed_letters)))}")
        print("=" * 30 + "\n")

        guess = input("Guess a letter: ").upper()

        # Input validation
        if not guess.isalpha() or len(guess) != 1:
            print("Invalid input. Please enter a single letter.")
            continue
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.")
            continue

        guessed_letters.add(guess)

        if guess in word_to_guess:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            incorrect_guesses += 1

        # Check for win condition
        word_guessed = True
        for letter in word_to_guess:
            if letter not in guessed_letters:
                word_guessed = False
                break

        if word_guessed:
            print("\n" + "=" * 30)
            print("Congratulations! You guessed the word!")
            print(f"The word was: {word_to_guess}")
            print("You won!")
            print("=" * 30 + "\n")
            break

    # Game over conditions
    if incorrect_guesses == guess_limit:
        print("\n" + "=" * 30)
        display_hangman(incorrect_guesses)  # Show the final hangman
        print("Game Over! You ran out of guesses.")
        print(f"The word was: {word_to_guess}")
        print("You lost!")
        print("=" * 30 + "\n")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == 'yes':
        hangman()
    else:
        print("Thanks for playing!")


if __name__ == "__main__":
    hangman()

