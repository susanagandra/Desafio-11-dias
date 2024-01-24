# Desenvolva um programa que seja capaz de gerar senhas aleatórias com critérios especificados pelo usuário, 
# como comprimento e inclusão de números, letras maiúsculas, letras minúsculas e caracteres especiais.

import string
import random

def create_random_password (length, use_numbers=True, use_uppercase=True, use_lowercase=True, use_special_chars=True):

    characters = ""

    if use_numbers:
        characters += string.digits
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_special_chars:
        characters += string.punctuation
    
    if not characters:
        print("Error! Selected at least one option.")
        return None
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Generated a random password.")

    length = int(input("How many characters do you want in your password: "))
    use_numbers = input("Include numbers? (Y/N): ").lower() == 'y'
    use_uppercase = input("Include uppercase letters? (Y/N): ").lower() == 'y'
    use_lowercase = input("Include lowercase letters? (Y/N): ").lower() == 'y'
    use_special_chars = input("Include special characters? (Y/N): ").lower() == 'y'

    password = create_random_password(length, use_numbers, use_uppercase, use_lowercase, use_special_chars)
    if password:
        print(f"\nYour generated password is: {password}")

if __name__ == "__main__":
    main()