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

### 3. `check_guess(guess, secret_word)` - The Main Challenge

Compare the guess to the secret word and return feedback.

- Return a list of 5 strings: `"correct"`, `"misplaced"`, or `"wrong"`
- Start with an empty list and build it up with `.append()`
- Loop through each position and ask, in order:
  1. Is this letter in the **right position**? → `"correct"`
  2. Otherwise, is this letter **somewhere** in the word? → `"misplaced"`
  3. Otherwise → `"wrong"`

Everything you need here is `for`, `if`/`elif`/`else`, the `in` operator, and list `.append()`.

**🌟 Bonus (optional, tricky!):** The simple version above has a subtle bug with
repeated letters. If the secret is `crane` and you guess `eerie`, both `e`s will
show yellow — but there's only one `e` in `crane`. Real Wordle only lights up as
many tiles as there are matching letters. Can you fix it? (Hint: keep track of
which letters you've already "used up.") A worked solution is in
`solutions/game_solution.py`.

### 4. `is_winner(guess, secret_word)` - Easy

Check if the player won (guess matches secret word exactly).

- Return `True` if they match, `False` otherwise

## Testing Your Code

### Option A: Test visually in the browser

1. Save your changes to `game.py`
2. Refresh your browser to see the results
3. Try these test cases:
   - Type a 3-letter word → Should say "Not enough letters"
   - Type "zzzzz" → Should say "Not in word list"
   - Type a valid word → Should show colored feedback

### Option B: Test quickly with `print()`

You don't have to launch the whole game every time. Add a few lines to the
**bottom** of `game.py` and run just that file with `uv run python game.py`:

```python
# Quick tests — delete before you're done!
print(is_five_letters("crane"))          # True
print(is_five_letters("hi"))             # False
print(is_winner("crane", "crane"))       # True
print(check_guess("brain", "crane"))     # ['wrong', 'correct', 'correct', 'wrong', 'misplaced']
```

Compare what prints to the comment on each line. This is the fastest way to
check `check_guess` since you can see the exact list it returns.

Good luck! 🎯
