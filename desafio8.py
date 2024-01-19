# Lista de Tarefas
# Desenvolva uma aplicação simples para gerenciar uma lista de tarefas, permitindo adicionar e remover itens.

list_items = []

while True:
    print("\n=== Menu ===")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. Show List")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == '1':
        new_item = input("Enter the new task: ")
        list_items.append(new_item)
        print(f"Task added successfully!")

    elif choice == '2':
        if (len(list_items) > 0 ):
            print("\nTask list:")
            for menu, task in enumerate(list_items):
                print(f"{menu}: {task}")       

            menu = int(input("\nTask to remove: "))
            
            if 0 <= menu < len(list_items):
                list_items.pop(menu)  
                print("\nThe task as remove.")
            else:
                print("\nInvalid task.")
        
        else:
            print("\nEmpty list.")

    elif choice == '3':
        
        if(len(list_items) > 0):
            print("\nTask list:")
            for menu, task in enumerate(list_items):
                print(f"{menu}: {task}")
        
        else:
            print("\nEmpty list.")


    elif choice == '4':
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please choose again.")
