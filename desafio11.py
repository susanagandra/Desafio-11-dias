# Desenvolva um script que ordene uma lista de números fornecida pelo usuário.


num_elements = (input("Insert the numbers you want, with a space between them, add too the list: "))

number_str = num_elements.split()  #divide a entrada the numeros numa lista de strings

numbers = [int(number) for number in number_str] #converte os números para inteiros

ordered_numbers = sorted(numbers)

print("Sorted List:", ordered_numbers)

