# Desenvolva um script que ordene uma lista de números fornecida pelo usuário.

def sort_numbers():

    numbers = []     # Initialize an empty list to store the numbers

    num_elements = int(input("How many numbers do you want to add to the list? "))


    for i in range(num_elements):        # Loop to receive numbers from the user
        number = float(input(f"Enter number {i + 1}: "))
        numbers.append(number)

    numbers.sort()


    print("\nOriginal List:", numbers)
    print("Sorted List:", numbers)

sort_numbers()

