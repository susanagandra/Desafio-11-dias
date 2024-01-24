# Desenvolva um script que verifique se uma string fornecida pelo usuário é um e-mail válido.
import re

def check_valid_email (email):

    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))

user_email = input("Please enter your email: ")

if check_valid_email(user_email):
    print(f"{user_email}  Valid email.")
else:
    print(f"{user_email} Invalid email.")
  