"""
Wordle Game Logic

This is the file you will edit! Implement the four functions below.
See README.md for full instructions and hints.
"""


def is_five_letters(guess):
    """Return True if guess has exactly 5 letters. E.g. "crane" -> True, "hi" -> False."""
    # TODO: Fix this function!
    return True


def is_valid_word(guess, valid_words):
    """Return True if guess is in valid_words. Hint: use the `in` operator."""
    # TODO: Fix this function!
    return True


def check_guess(guess, secret_word):
    """
    Return a list of 5 strings comparing guess to secret_word, one per letter:
    "correct" (right letter, right spot), "misplaced" (in word, wrong spot),
    or "wrong" (not in word).

    E.g. check_guess("brain", "crane") -> ["wrong", "correct", "correct", "wrong", "misplaced"]
    """
    # TODO: Fix this function!
    return ["wrong", "wrong", "wrong", "wrong", "wrong"]


def is_winner(guess, secret_word):
    """Return True if guess exactly matches secret_word."""
    # TODO: Fix this function!
    return False
