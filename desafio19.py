#Crie um programa que funcione como uma agenda de contatos. 
#Deve ser possível adicionar, listar, buscar e excluir contatos. Cada contato deve ter nome, número de telefone e e-mail.


import csv
import os

def add_contact():
    name = input("Nome: ")
    telephone = input("Número de telefone: ")
    email = input("Email: ")

    with open('contact.csv', mode='a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([name, telephone, email])

    print("Contato inserido com sucesso!")

def delete_contacts():
    name_to_delete = input("Digite o nome do contato que deseja excluir: ")
    contacts = []
    
    try:
        with open('contact.csv', mode='r') as csv_file:
            reader_csv = csv.reader(csv_file)
            for row in reader_csv:
                if row[0].lower() != name_to_delete.lower():
                    contacts.append(row)

        with open('contact.csv', mode='w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(contacts)

        print(f"Contato '{name_to_delete}' excluído com sucesso!")
    except FileNotFoundError:
        print("Não existe lista de contatos.")
        

def search_contact():
    name_to_search = input("Digite o nome do contato que deseja buscar: ")
    
    try:
        with open('contact.csv', mode='r') as csv_file:
            reader_csv = csv.reader(csv_file)
            found = False
            for row in reader_csv:
                if row[0].lower() == name_to_search.lower():
                    print(f"Nome: {row[0]}, Telefone: {row[1]}, Email: {row[2]}")
                    found = True

            if not found:
                print(f"Contato '{name_to_search}' não encontrado.")
    except FileNotFoundError:
        print("Não existe lista de contatos.")

def show_contacts():
    try:
        with open('contact.csv', mode='r') as csv_file:
            reader_csv = csv.reader(csv_file)
            print("\n---- Lista de contatos ----")
            for row in reader_csv:
                print(f"Nome: {row[0]}, Telefone: {row[1]}, Email: {row[2]}")
    except FileNotFoundError:
        print("Não existe lista de contatos.")

while True:
    print("\n--- Lista de Contatos ---")
    print("1. Adicionar contato")
    print("2. Excluir contato")
    print("3. Buscar contato")
    print("4. Ver lista de contatos")
    print("5. Sair")

    choice = input("Opção: ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        delete_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        show_contacts()
    elif choice == '5':
        break
    else:
        print("Opção inválida!")
