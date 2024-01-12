#Desenvolva um programa que peça ao usuário para inserir um número. O programa deve então verificar se 
# o número é par ou ímpar e exibir uma mensagem informando o usuário.


# inserir o numero. A função input obtem um valor inserido. 
# int() converte o valor num numero inteiro.


num = int(input("Por favor, insira um número: "))


# verifica se o numero é par ou impar

if num % 2 == 0:
    print(f"O número {num} é par.")
else:
    print(f"O número {num} é ímpar.")

