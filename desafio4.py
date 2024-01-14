# Desenvolva um programa que conte o número de palavras em um texto fornecido pelo usuário. O programa deve ser capaz 
# de separar as palavras em um texto e determinar quantas palavras estão presentes.


def words_count (text):

    words = text.split()    #divide o texto em palavra

    num_words = len(words)   #conta o numero de palavras

    return num_words

user_text = input("Texto: ")


result = words_count(user_text)

print(f'Este texto tem {result} palavras')

