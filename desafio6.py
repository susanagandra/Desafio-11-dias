# Crie um programa que converta unidades de medida. Para este desafio o foco são as conversões de Quilômetros para Milhas, 
# Milhas para Quilômetros, Metros para Pés, Pés para Metros, Graus Celsius para Fahrenheit e Graus Fahrenheit para Celsius.


def convert_km_in_miles(km) :
    miles =  km * 0.621371
    return miles

def convert_miles_in_km(miles) :
    km =  miles / 0.621371
    return km

def convert_meters_in_feet(meter) :
    feet =  meter * 3.28084
    return feet

def convert_feet_in_meter(feet) :
    meter =  feet / 3.28084
    return meter

def convert_celsius_in_fahrenheit(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

def convert_fahrenheit_in_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9 
    return celsius


print("Conversão:")
print("1. Quilômetros para Milhas")
print("2. Milhas para Quilômetros")
print("3. Metros para Pés")
print("4. Pés para Metros")
print("5. Celsius para Fahrenheit")
print("6. Fahrenheit para Celsius")

option = int(input("Tipo de conversão: "))
value= float(input("Valor a ser convertido: "))

if option == 1:
    result = convert_km_in_miles(value)
    print(f"{value} quilômetros é igual a {result} milhas")
elif option == 2:
    result = convert_miles_in_km(value)
    print(f"{value} milhas é igual a {result} quilômetros")
elif option == 3:
    result = convert_meters_in_feet(value)
    print(f"{value} metros é igual a {result} pés")
elif option == 4:
    result = convert_feet_in_meter(value)
    print(f"{value} pés é igual a {result} metros")
elif option == 5:
    result = convert_celsius_in_fahrenheit(value)
    print(f"{value} graus Celsius é igual a {result} graus Fahrenheit")
elif option == 6:
    result = convert_fahrenheit_in_celsius(value)
    print(f"{value} graus Fahrenheit é igual a {result} graus Celsius")
else:
    print("Opção inválida. Por favor, escolha uma opção de 1 a 6.")

