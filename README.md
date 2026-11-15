
# Hangman Word Guessing Game

## Project Overview
This project is a terminal-based Hangman word guessing game developed using Python as part of the Datheon Python Programming Internship.

The player must guess a randomly selected hidden word by entering one letter at a time. The player gets a maximum of six incorrect attempts.

## Features
- Random word selection.
- Hidden letters displayed as underscores.
- Interactive letter guessing.
- ASCII Hangman gallows that updates after incorrect guesses.
- Tracks previously guessed letters.
- Prevents duplicate guesses from reducing attempts.
- Displays winning and losing messages.

## Technologies Used
- Python 3.14
- Random module
- VS Code

## Project Structure

```text
Task_1_Hangman/
│
├── hangman.py
└── README.md
```

## How to Run the Project

1. Install Python 3.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Execute:

```bash
python hangman.py
```

## Game Rules
1. The computer selects a random word.
2. The player guesses one letter at a time.
3. Correct guesses reveal matching letters.
4. Incorrect guesses update the Hangman drawing.
5. The player loses after six incorrect guesses.
6. The player wins by guessing all letters correctly.

## Expected Outcome
An interactive terminal-based Hangman game with progressive ASCII gallows and input validation.

## Internship
Datheon Python Programming Internship
