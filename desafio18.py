#Desenvolva um programa que converta valores entre diferentes moedas. 
#O programa deve permitir ao usuário inserir o valor, a moeda de origem e a moeda de destino, 
#e então mostrar o valor convertido utilizando uma api pública que traz a taxa para a conversão.

import requests


def currency_exchange_rate(value, origin_currency, convert_currency):

    url = f"https://open.er-api.com/v6/latest/{origin_currency}"
    
    try:
        fetch_get = requests.get(url)                    # Faz a requisição HTTP para obter as taxas de câmbio
        data = fetch_get.json()


        if data["result"] == "error":                   # Verifica se a moeda de origem é válida
            return "\nMoeda de origem inválida.\n"


        if convert_currency not in data["rates"]:       # Verifica se a moeda de destino é válida
            return "\nMoeda de destino inválida.\n"

        
        if valor <= 0:                                  # Verifica se o valor é válido (deve ser um número positivo)
            return "\nValor inválido.\n"

        
        exchange_fee = data["rates"][convert_currency]     # Calcula a taxa de conversão e o valor convertido
        value_convert = value * exchange_fee
        return f"\nResultado da conversão: {value_convert:.2f} {convert_currency}\n"

    except requests.exceptions.RequestException:
        return "\nErro na conexão com a API.\n"
    except ValueError:
        return "\nValor inválido.\n"


def main():
    print("\n### Conversor de Moedas ###\n")
    
    
    value = input("Digite o valor a ser convertido: ")
    try:
        value = float(value)
    except ValueError:
        print("\nValor inválido.\n")
        return

    origin_currency = input("Digite a moeda de origem (por exemplo, USD): ").upper()
    convert_currency = input("Digite a moeda de destino (por exemplo, EUR): ").upper()

    # Chama a função de conversão e imprime o resultado
    result = currency_exchange_rate(value, origin_currency, convert_currency)
    print(result)

if __name__ == "__main__":
    main()
