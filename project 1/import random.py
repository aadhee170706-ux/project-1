import random

HANGMAN_PICS = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]

WORDS = {
    "easy": ["apple", "robot", "sun", "cat", "blue"],
    "medium": ["python", "banana", "jazz", "window", "planet"],
    "hard": ["hangman", "xylophone", "sphinx", "crypt", "dwarves"]
}

def get_word(difficulty):
    """Returns a random word based on the difficulty."""
    return random.choice(WORDS[difficulty])

def display_game_state(display, wrong_guesses):
    """Shows the hangman image and current word progress."""
    print(HANGMAN_PICS[wrong_guesses])
    print("Word: ", " ".join(display))
    print(f"Wrong guesses: {wrong_guesses}/6")

def play_round():
    """Plays a single game of Hangman."""
    print("Choose difficulty: easy / medium / hard")
    difficulty = input("Your choice: ").lower()

    if difficulty not in WORDS:
        print("Invalid choice. Defaulting to EASY.")
        difficulty = "easy"

    secret_word = get_word(difficulty)
    display = ["_"] * len(secret_word)
    guessed = []
    wrong = 0

    print("\nLet's play Hangman!")

    while wrong < 6 and "_" in display:
        display_game_state(display, wrong)
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed:
            print("You already guessed that letter.")
            continue

        guessed.append(guess)

        if guess in secret_word:
            print("Correct!")
            for i, letter in enumerate(secret_word):
                if letter == guess:
                    display[i] = guess
        else:
            print("Wrong!")
            wrong += 1

    display_game_state(display, wrong)
    if "_" not in display:
        print("\n🎉 CONGRATS! You guessed the word:", secret_word)
    else:
        print("\n❌ GAME OVER! The word was:", secret_word)

def main():
    """Main loop for replaying game."""
    while True:
        play_round()
        again = input("\nPlay again? (y/n): ").lower()
        if again != "y":
            print("Thanks for playing!")
            break
main()