# Desenvolva um jogo que gera aleatoriamente um número e o jogador deve determinar se esse número é primo ou não. 
# O jogador ganha pontos por cada resposta correta.

import random

def is_prime(number):
    if number < 2:
        return False
    
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def play_game():
    score = 0
    rounds = 5  # Defina o número de rodadas desejado

    print("Bem-vindo ao Números Primos - O Jogo!")


    for _ in range(rounds):
        random_number = random.randint(1, 100)
        print(f"\nNúmero: {random_number}")

        user_input = input("É primo? (S/N): ").strip().lower()

        if (user_input == 's' and is_prime(random_number)) or (user_input == 'n' and not is_prime(random_number)):
            print("Resposta correta! +1 ponto\n")
            score += 1
        else:
            print(f"Errado! O número {random_number} {'é' if is_prime(random_number) else 'não é'} primo.\n")

    print(f"Game over! Total de pontos: {score}")

def view_score(current_score):
    print(f"\nPontuação: {current_score}\n")

def reset_score():
    return 0

if __name__ == "__main__":
    score = 0

    while True:
        print("\n=== MENU ===")
        print("1. Jogar")
        print("2. Pontuação")
        print("3. Iniciar jogo")
        print("4. Sair")

        choice = input("Escolha a opção (1-4): ").strip()

        if choice == '1':
            score += play_game()
        elif choice == '2':
            view_score(score)
        elif choice == '3':
            score = reset_score()
            print("Novo jogo.")
        elif choice == '4':
            print("Até à próxima!")
            break
        else:
            print("Opção inválida.")