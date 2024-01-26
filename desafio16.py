# Desenvolva uma versão simples do jogo da forca, onde o usuário tenta adivinhar uma palavra escolhida 
# aleatoriamente pelo programa.
import random


def random_word():
    words =['game', 'python', 'challenge', 'programming', 'love']

    return random.choice(words)


def display_word(word, guessed_letters):

    display= ""

    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    
    return display

def hangman():
    word_to_guess = random_word()
    guessed_letters = []
    max_attempts = 10
    attempts = 0

    print("Welcome to Hangman!")

    while True:
            current_display = display_word(word_to_guess, guessed_letters)
            print(f"Current word: {current_display}")
            guess = input("Guess a letter: ").lower()

            if guess in guessed_letters:
                print("You already guessed that letter. Try again.")
                continue

            guessed_letters.append(guess)

            if guess not in word_to_guess:
                attempts += 1
                print(f"Incorrect guess! Attempts remaining: {max_attempts - attempts}")
                if attempts == max_attempts:
                    print(f"Sorry, you ran out of attempts. The correct word was '{word_to_guess}'.")
                    break
            else:
                print("Correct guess!")

            if set(guessed_letters) == set(word_to_guess):
                print(f"Congratulations! You guessed the word: '{word_to_guess}'.")
                break

if __name__ == "__main__":
    hangman()