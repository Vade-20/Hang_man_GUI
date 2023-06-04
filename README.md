# Hangman Game

The Hangman Game is a classic word-guessing game implemented using Python and Tkinter. Players try to guess a hidden word by guessing letters one by one. This game provides a graphical user interface (GUI) using Tkinter, making it easy and enjoyable to play.

## Prerequisites

- Python 3.x
- Tkinter library
- PyDictionary library

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Vade-20/Hang_man_GUI.git
   ```

2. Install the required libraries:

   ```bash
   pip install tkinter
   pip install PyDictionary
   ```

## Usage

1. Run the Python script:

   ```bash
   python hangman_game.py
   ```

2. The game window will appear, showing a "Start Game" button.

3. Click the "Start Game" button to begin a new game.

4. A random word will be chosen, and its meaning will be displayed on the screen.

5. Guess the word by entering a letter in the entry box or selecting a letter from the drop-down menu.

6. The game will indicate whether the guess is correct or not. If correct, the corresponding letters will be revealed in the word.

7. The game provides 7 chances to guess the word. For each incorrect guess, a body part of the hangman will be displayed.

8. If all the letters are correctly guessed within the given chances, you win the game. Otherwise, you lose.

9. You can start a new game at any time by clicking the "New Game" button or pressing Enter key on keyboard.

