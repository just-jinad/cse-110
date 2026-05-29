# CSE 110 - Word Puzzle
# Author: Tope Jinad

secret_word = "mosiah"

print("Welcome to the word guessing game!")
print()

hint = ""
for letter in secret_word:
    hint = hint + "_ "

guess_count = 0

print("Your hint is: " + hint)

guess = input("What is your guess? ").lower()
guess_count = guess_count + 1

while guess != secret_word:

    if len(guess) != len(secret_word):
        print("Sorry, the guess must have the same number of letters as the secret word.")
        print()
    else:
        hint = ""
        for i in range(len(secret_word)):
            if guess[i] == secret_word[i]:
                hint = hint + guess[i].upper() + " "
            elif guess[i] in secret_word:
                hint = hint + guess[i].lower() + " "
            else:
                hint = hint + "_ "

        print("Your hint is: " + hint)

    guess = input("What is your guess? ").lower()
    guess_count = guess_count + 1

print("Congratulations! You guessed it!")
print(f"It took you {guess_count} guesses.")