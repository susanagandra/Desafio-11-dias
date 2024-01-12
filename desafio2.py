# Desenvolva um programa que realize operações básicas de matemática, como adição, subtração, multiplicação e divisão.


def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def multi(num1, num2):
    return num1 * num2

def div(num1, num2):
    if num2 != 0 :
        return num1 / num2
    else :
         print(f"Erro na divisão")


num1 = float(input("Insira o primeiro número: "))

num2 = float(input("Insira o segundo número: "))

operation = input("Digite a operação desejada (+, -, *, /): ")

# Executar a operação escolhida

if operation == '+':
    result = add(num1, num2)

elif operation == '-':
    result = sub(num1, num2)

elif operation == '*':
    result = multi(num1, num2)

elif operation == '/':
    result = div(num1, num2)

else:
    result = "Operação inválida"


print(f"Resultado: {result}")