import random

# List of predefined words
words = ["apple", "banana", "cherry", "orange", "grape"]

# Choose a random word
word = random.choice(words)
guessed_letters = []
wrong_guesses = 0
max_wrong = 6

print("Welcome to Hangman Game!")

while wrong_guesses < max_wrong:
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word.strip())

    # Check if user has guessed the whole word
    if "_" not in display_word:
        print("🎉 Congratulations! You guessed the word correctly.")
        break

    guess = input("Guess a letter: ").lower()

    # Validation
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess not in word:
        wrong_guesses += 1
        print(f"Wrong guess! Remaining attempts: {max_wrong - wrong_guesses}")
    else:
        print("Good guess!")

# If player loses
if wrong_guesses == max_wrong:
    print("\n❌ Game Over!")
    print("The word was:", word)
