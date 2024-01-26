# Desenvolva um programa em Python que permita ao usuário inserir informações sobre livros em sua biblioteca pessoal e, 
# em seguida, visualizar a lista de livros disponíveis.

import csv

def add_book(title, author, year):
    title = input("Enter the title of the book: ")
    author = input("Enter the author's name: ")
    year = input("Enter the publication year: ")
    add_book(title, author, year)

    add_book(title, author, year)
    print("Book added successfully!")


    with open('library.csv', mode='a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([title, author, year])


def view_library():
    try:
        with open('library.csv', mode='r') as csv_file:
            reader_csv= csv.reader(csv_file)
            print("\n--- Library ---")
            for row in reader_csv:
                print(f"Título: {row[0]}, Autor: {row[1]}, Ano: {row[2]}")
    except FileNotFoundError:
        print("\nA The library is empty.")


while True:
    print("\n--- Menu ---")
    print("1. Add a book")
    print("2. View the library")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == '1':
        add_book()

    elif choice == '2':
        view_library()

    elif choice == '3':
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid option. Please try again.")
