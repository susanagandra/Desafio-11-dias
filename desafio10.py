# Desenvolva um jogo de adivinhação em que o usuário deve adivinhar um número gerado aleatoriamente pelo programa. 
# O jogo deve ter as seguintes características:
#    O programa gera um número aleatório entre 1 e 100.
#    O jogador tem um número limitado de tentativas (7) para adivinhar o número correto.
#    Após cada tentativa, o programa fornece dicas sobre se o número correto é maior ou menor do que a tentativa atual do jogador.
#    O jogo continua até que o jogador adivinhe corretamente o número ou esgote todas as tentativas.

import random

def play_guess_number ():
     random_number = random.randint(1, 100)

     num_attempts = 7
     number_player = 0

     print("welcome to the game of Guess the Number!")
     print("Guess a number between 1 and 100.")

     while number_player < num_attempts:

        play = int(input("Guess the number: "))

        if play == random_number:
             print(f"Congrats!!! You guess the right number in {num_attempts} attempts.")
             break
        elif play < random_number:
              print("Wrong number. Pick bigger number.")
        else:
             print("Wrong number. Pick a lower number.")

        number_player += 1
    
        if num_attempts == number_player:
            print(f"You don't have more attempts to guess the number. The correct number as {random_number}.")


play_guess_number()
            



    
