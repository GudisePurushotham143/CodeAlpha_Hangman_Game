import random

words = ["apple", "python", "mango", "orange", "banana"]

word = random.choice(words)

guessed = []

attempts = 6

print("Welcome to Hangman Game!")

while attempts > 0:

    display = ""

    for letter in word:
        if letter in guessed:
            display += letter
        else:
            display += "_"

    print(display)

    if "_" not in display:
        print("Congratulations! You Won!")
        break

    guess = input("Enter a letter: ").lower()

    guessed.append(guess)

    if guess not in word:
        attempts -= 1
        print("Wrong Guess!")
        print("Remaining Chances:", attempts)

if attempts == 0:
    print("Game Over!")
    print("Correct Word:", word)