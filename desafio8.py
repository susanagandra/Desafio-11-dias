# Lista de Tarefas
# Desenvolva uma aplicação simples para gerenciar uma lista de tarefas, permitindo adicionar e remover itens.

list_items = []

def add_item(item):
    list_items.append(item)
    print(f"Item '{item}' added successfully!")

def remove_item():
    if list_items:
        removed_item = list_items.pop()
        print(f"Item '{removed_item}' removed successfully!")
        return removed_item
    else:
        print("This list is empty! Nothing to remove.")

    return list_items

while True:
    print("\n=== Menu ===")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. Show List")
    print("4. Exit")

    choice = input("Choose an option (1/2/3/4): ")

    if choice == '1':
        new_item = input("Enter the item to add: ")
        add_item(new_item)
    elif choice == '2':
        removed_item = remove_item()
        if removed_item:
            print(f"Removed item: {removed_item}")
    elif choice == '3':
        current_list = show_list()
        print("Current List:", current_list)
    elif choice == '4':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please choose again.")