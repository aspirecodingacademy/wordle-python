# Wordle

Build your own Wordle game by implementing the game logic in Python!

## Getting Started

### Option 1: GitHub Codespaces (Recommended)
1. Click the green "Code" button on GitHub
2. Select "Open with Codespaces"
3. Wait for the environment to load

### Option 2: Local Setup
1. Make sure you have Python 3.11+ installed
2. Install dependencies: `pip install -r requirements.txt`

## Running the Game

Start the server:
```bash
python app.py
```

Then open your browser to: http://localhost:5000

## Your Task

Edit `game.py` to implement these functions:

### 1. `is_five_letters(guess)`
Check if the guess has exactly 5 letters.

### 2. `is_valid_word(guess, valid_words)`
Check if the guess is a real word in our word list.

### 3. `check_guess(guess, secret_word)`
Compare the guess to the secret word and return feedback:
- `"correct"` = right letter, right position (green)
- `"misplaced"` = right letter, wrong position (yellow)
- `"wrong"` = letter not in word (gray)

### 4. `is_winner(guess, secret_word)`
Check if the player won (guess matches secret word).

## Testing Your Code

After making changes to `game.py`, refresh your browser to test. The game will show you visual feedback based on your functions!
