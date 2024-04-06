import json
import time
import os

#include a daily save feature/pick somthing daily to save/break a bad habit
#include a monthly income
#include a static bank amount

def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})
    with open('expenses.json', 'w') as f:
        json.dump(expenses, f)
            
def print_expenses(expenses):
    for i, expense in enumerate(expenses):
        print(f'{i + 1}. Amount: {expense["amount"]}, Category: {expense["category"]}')
        
    while True:
        choice = input('Enter the number of the expense you want to delete(list#), or press Enter to cancel.: ')
        if choice == '':
            break
        try:
            index = int(choice) - 1
            if 0 <= index < len(expenses):
                del expenses[index]
                with open('expenses.json', 'w') as f:
                    json.dump(expenses, f)
                break
            else:
                print('Invalid choice. Please enter a valid number.')
        except ValueError:
            print('Invalid choice. Please enter a valid number.')
                    
def total_expenses(expenses):
    return sum(map(lambda expense: expense['amount'], expenses))
    
def filter_expenses_by_category(expenses, category):
    return filter(lambda expense: expense['category'] == category or input('Enter a new category name or press Enter to keep the current category): ') != '', expenses)
    

def main():
    expenses = []
    #checks if a file named 'expenses.json exists to store input data.
    if not os.path.exists("expenses.json"):
        print('No data found! check if "expenses.json" exists.')
    else:    
        with open('expenses.json', 'r') as f:
            expenses = json.loads(f.read())

    while True:
        print('\nExpense Tracker')
        time.sleep(1)
        print('1. Add an expense')
        # #2 will give option to delete expenses.
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit.')
        choice = input('Enter your choice: ')

        if choice == '1':
            amount = float(input('Enter amount: '))
            category = input('Enter category: ')
            add_expense(expenses, amount, category)

        elif choice == '2':
            print('\nAll Expenses:')
            print_expenses(expenses)

        elif choice == '3':
            print('\nTotal Expenses: ', total_expenses(expenses))

        elif choice == '4':
            category = input('Enter category to filter: ')
            print(f'\nExpenses for {category}:')
            expenses_from_category = filter_expenses_by_category(expenses, category)
            print_expenses(expenses_from_category)

        elif choice == '5':
            print('Exiting the program.')
            time.sleep(2)
            print('Goodbye!!')
            time.sleep(1)
            break

if __name__ == '__main__':
    main()