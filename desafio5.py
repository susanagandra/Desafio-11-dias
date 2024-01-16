import random

# Desenvolva um script que gere e exiba uma lista com 6 números aleatórios entre 1 e 60, sem repetições (ou seja, dentre os seis números selecionados, 
# não podem existir números repetidos), para que você possa fazer um jogo da Mega Sena.

mega_numbers = []

while len(mega_numbers) < 6:

    num = random.randint(1, 60) #gera um numero aleatório 1-60

    if num not in mega_numbers:     #verifica se o numero está na lista
        mega_numbers.append(num)    #adiciona se não estiver presente

print ("os seus números são:", mega_numbers)


