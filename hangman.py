import random

# List of words
words = [
    "python", "computer", "programming", "developer",
    "keyboard", "monitor", "internet", "hangman",
    "github", "algorithm"
]

# Choose a random word
word = random.choice(words)

# Variables
guessed_letters = []
incorrect_guesses = 0
max_attempts = 6

print("=" * 40)
print("        WELCOME TO HANGMAN WORLD")
print("=" * 40)

while True:
    # Display the current word
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check if player has guessed the word
    if "_" not in display_word:
        print("\n🎉 Congratulations! You guessed the word:", word)
        break

    print(f"Attempts Left: {max_attempts - incorrect_guesses}")
    print("Guessed Letters:", " ".join(guessed_letters))

    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one  alphabet letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that  letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Correct!")
    else:
        incorrect_guesses += 1
        print("❌ Wrong!")

    if incorrect_guesses == max_attempts:
        print("\n💀 Game Over!")
        print("The correct word was:", word)
        break
