
import random

# 1. Word collection
words = ["APPLE", "TIGER", "RIVER", "EARTH", "MANGO"]

# 2. Select a random word
secret_word = random.choice(words)

# 3. Initialize game variables
display = ["_"] * len(secret_word)
attempts = 6
guessed_letters = []

# 4. ASCII gallows stages
hangman_stages = [
    """
       +---+
       |   |
           |
           |
           |
      =======
    """,
    """
       +---+
       |   |
       O   |
           |
           |
      =======
    """,
    """
       +---+
       |   |
       O   |
       |   |
           |
      =======
    """,
    """
       +---+
       |   |
       O   |
      /|   |
           |
      =======
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
           |
      =======
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
      /    |
      =======
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
      / \\  |
      =======
    """
]

print("=" * 35)
print("       WELCOME TO HANGMAN")
print("=" * 35)

# 5. Main game loop
while attempts > 0 and "_" in display:

    print("\n" + hangman_stages[6 - attempts])
    print("Word:", " ".join(display))
    print("Attempts remaining:", attempts)
    print("Previously guessed:", guessed_letters)

    # Get user input
    guess = input("\nEnter a letter: ").strip().upper()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet letter.")
        continue

    # Prevent duplicate guesses
    if guess in guessed_letters:
        print("You already guessed this letter. Try another.")
        continue

    guessed_letters.append(guess)

    # Check the guessed letter
    if guess in secret_word:

        print("Correct guess!")

        # Reveal every matching occurrence
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display[i] = guess

    else:
        attempts -= 1
        print("Wrong guess!")

# 6. Final result
print("\n" + hangman_stages[6 - attempts])
print("\nWord:", " ".join(display))

if "_" not in display:
    print("\nCONGRATULATIONS! YOU WON!")
else:
    print("\nGAME OVER! YOU LOST!")

print("The correct word was:", secret_word)
print("=" * 35)

    



