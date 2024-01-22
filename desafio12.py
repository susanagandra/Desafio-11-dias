#Desenvolva um programa que analise a frequência de cada letra em um texto fornecido pelo usuário.


def text_letter_frequency (text):

    text = text.lower()

    letter_frequency = {}

    for char in text:

        if char.isalpha():     #verifica se o caracter é alfabetica

            letter_frequency[char] = letter_frequency.get(char, 0) + 1  #incrementa a letra
    
    print("Letter frequencies:")
    for letter, frequency in sorted(letter_frequency.items()):
        print(f"{letter}: {frequency}")

text_input = input("Insert the text to analyze: ")

text_letter_frequency(text_input)







