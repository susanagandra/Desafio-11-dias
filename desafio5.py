import random

# Desenvolva um script que gere e exiba uma lista com 6 números aleatórios entre 1 e 60, sem repetições (ou seja, dentre os seis números selecionados, 
# não podem existir números repetidos), para que você possa fazer um jogo da Mega Sena.


def num_mega():
    random_num = []

    while len(random_num) < 6:
        num = random.randint(1, 60)

        # Verifica se o número já foi gerado
        if num not in random_num:
            random_num.append(num)

    return random_num

def show_num_mega(nums):
    print("Os seus números:")
    for num in nums:
        print(num)

num_mega_created = num_mega()
show_num_mega(num_mega_created)

