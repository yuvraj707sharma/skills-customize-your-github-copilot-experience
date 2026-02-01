
# 📘 Assignment: Games in Python

## 🎯 Objective

Build the classic Hangman word-guessing game using Python to practice string manipulation, loops, conditionals, and random selection.

## 📝 Tasks

### 🛠️ Implement Game Setup and Word Selection

#### Description
Create the initial setup for your Hangman game, including a word list and logic to randomly select a word for the player to guess.

#### Requirements
Completed program should:

- Store a list of at least 10 words to choose from
- Use the `random` module to select a word
- Initialize game variables (incorrect guesses remaining, guessed letters)
- Display the initial hidden word state (underscores: `_ _ _ _ _`)


### 🛠️ Handle Player Guesses

#### Description
Write functions to process player letter guesses and update the game state accordingly.

#### Requirements
Completed program should:

- Accept single letter input from the player
- Check if the letter exists in the word
- Track guessed letters and prevent duplicate guesses
- Update the display showing revealed letters in correct positions
- Decrement attempts if the guess is incorrect
- Display feedback (correct/incorrect) for each guess


### 🛠️ Manage Win/Lose Conditions

#### Description
Implement game logic to determine when the player wins or loses and end the game appropriately.

#### Requirements
Completed program should:

- End the game when all letters are guessed (win)
- End the game when attempts reach zero (lose)
- Display appropriate win/lose messages
- Show the final word when the game ends
- Offer to play again or exit
