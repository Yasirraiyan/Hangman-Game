import random

# List of words to choose from
words = ['father', 'mother', 'brother']
# Randomly select a word from the list
chosen_word = random.choice(words)  
score = 0
chances = 3

print("Welcome to the Hangman game!")

# Game loop for guessing
while chances > 0:
    guess = input("Guess a word: ").strip().lower()  # Get user input and normalize it

    # Check if the guessed word matches the chosen word
    if guess == chosen_word:
        print("Your guess is correct!")
        score += 1  # Increment score
        print(f"Your current score is: {score}")  # Show current score
        break  # Exit the loop since the guess was correct
    else:
        print("Wrong guess!")
        chances -= 1  # Decrement chances
        print(f"Chances left: {chances}")

        # Check if there are no chances left
        if chances == 0:
            print("Game over! The correct word was:", chosen_word)

# Display the final score
print(f"Your final score is: {score}")
