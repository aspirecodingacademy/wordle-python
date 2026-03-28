# Wordle

Build your own Wordle game by implementing the game logic in Python!

## Running the Game

Start the server:

```
uv run python app.py
```

Then click the URL that appears

## Game Rules

Guess the secret 5-letter word in 6 tries!

After each guess, tiles change color:

- 🟩 **Green** = Correct letter in the correct spot
- 🟨 **Yellow** = Correct letter but wrong spot
- ⬛ **Gray** = Letter not in the word

## Your Task

Edit `game.py` to implement these four functions:

### 1. `is_five_letters(guess)` - Easy

Check if the guess has exactly 5 letters.

- Return `True` if it does, `False` otherwise

### 2. `is_valid_word(guess, valid_words)` - Easy

Check if the guess is a real word in our word list.

- Return `True` if the word is valid, `False` otherwise

### 3. `check_guess(guess, secret_word)`

Compare the guess to the secret word and return feedback.

- Return a list of 5 strings: `"correct"`, `"misplaced"`, or `"wrong"`
- Loop through each letter and check: right position? in the word? or not at all?

### 4. `is_winner(guess, secret_word)` - Easy

Check if the player won (guess matches secret word exactly).

- Return `True` if they match, `False` otherwise

## Testing Your Code

1. Save your changes to `game.py`
2. Refresh your browser to see the results
3. Try these test cases:
   - Type a 3-letter word → Should say "Not enough letters"
   - Type "zzzzz" → Should say "Not in word list"
   - Type a valid word → Should show colored feedback

Good luck! 🎯
