#Crie um programa em Python que funcione como uma calculadora de despesas pessoais. 
#O programa deve permitir ao usuário registrar suas despesas diárias, categorizá-las e, em seguida, gerar um resumo 
#das despesas por categoria e o total das despesas de uma data específica.

import csv
from datetime import datetime

expenses = []

def show_menu():
    print("Personal Expense Calculator")
    print("1. Add Expense")
    print("2. View Expenses by Category")
    print("3. View Total Expenses for a Date")
    print("4. Exit")

def add_expense():
    date = datetime.now().strftime('%Y-%m-%d')
    category = input("Enter expense category: ")
    amount = float(input("Enter expense amount: "))
    expenses.append({"date": date, "category": category, "amount": amount})
    print("Expense added successfully!")

def view_expenses_by_category():
    category = input("Enter category to view expenses: ")
    category_expenses = [expense for expense in expenses if expense["category"].lower() == category.lower()]
    
    if category_expenses:
        print(f"Expenses for {category.capitalize()} category:")
        for expense in category_expenses:
            print(f"{expense['date']} - {expense['amount']:.2f}€")
    else:
        print(f"No expenses found for {category.capitalize()} category.")

def view_total_expenses_for_date():
    date = input("Enter date to view total expenses (YYYY-MM-DD): ")
    total_expenses = sum(expense["amount"] for expense in expenses if expense["date"] == date)
    print(f"Total expenses for {date}: {total_expenses:.2f}€")

def save_to_csv():
    with open('expenses.csv', 'w', newline='') as csv_file:
        fieldnames = ['date', 'category', 'amount']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        
        writer.writeheader()
        for expense in expenses:
            writer.writerow(expense)

def load_from_csv():
    try:
        with open('expenses.csv', newline='') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                expenses.append({"date": row['date'], "category": row['category'], "amount": float(row['amount'])})
    except FileNotFoundError:
        pass

# Load existing expenses from CSV file (if any)
load_from_csv()

while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        add_expense()
    elif choice == '2':
        view_expenses_by_category()
    elif choice == '3':
        view_total_expenses_for_date()
    elif choice == '4':
        save_to_csv()
        print("Exiting. Have a great day!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
