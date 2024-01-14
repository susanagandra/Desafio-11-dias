# Crie um script que verifica se uma palavra ou frase fornecida pelo usuário é um palíndromo. 
# Palíndromo é uma palavra ou uma frase que de frente pra trás e de trás pra frente são iguais, por exemplo, "ovo", "radar" e "Ame o poema".


def is_palindrome(text):
    
    format_text = ''.join(filter(str.isalnum, text)).lower() #remove espaços, coloca tudo em minúsculo

    return format_text == format_text[::-1]   #verifica se é palíndromo


user_text = input ("Escreva um texto ou palavra: ")


if is_palindrome(user_text):
    print(f'É um palíndromo.')

else:
    print(f'Não é um palíndromo.')




