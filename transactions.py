import json
current_balance = 0.0
all_transactions = []  # List that will hold all transactions

def add_income():
    global all_transactions
    while True:
        try:
            income = float(input("Enter the amount of income: "))  # Taking income input
            break  # If conversion to float is successful, break the loop
        except ValueError:  # If conversion to float fails, print an error message and continue the loop
            print("Invalid input. Please enter a numeric value.")
    description = input("Enter a description for this income: ")  # Taking description of income

    all_transactions.append({
        "type": "income",
        "amount": income,
        "description": description
    })

    print(f"You added an income of {income} for {description}. Keep going!")

def add_expense():
    global all_transactions
    while True:
        try:
            expense = float(input("Enter the amount of expense: "))  # Taking expense input
            break  # If conversion to float is successful, break the loop
        except ValueError:  # If conversion to float fails, print an error message and continue the loop
            print("Invalid input. Please enter a numeric value.")
    description = input("Enter a description for this expense: ")  # Taking description of expense

    all_transactions.append({
        "type": "expense",
        "amount": expense,
        "description": description
    })

    print(f"You added an expense of {expense} for {description}.")

def view_all_transactions():
    global all_transactions  # Accessing global variable
    # Loop through all transactions and print them
    for index, transaction in enumerate(all_transactions, start=1):
        print(f"{index}. {transaction['type']}: {transaction['amount']} ({transaction['description']})")

def delete_transaction():
    global all_transactions
    # Show all transactions to user for deleting
    view_all_transactions()
    transaction_number = int(input("Enter the number of the transaction you want to delete: "))  # Taking transaction number input from user for deleting
    transaction = all_transactions.pop(transaction_number - 1)  # Removes and returns the transaction at the specified index

    print(f"You have deleted a {transaction['type']} of {transaction['amount']} ({transaction['description']})")

def get_total_income():
    """
    This function calculates the total income.
    It iterates over all transactions, and for each transaction that is of type 'income',
    it adds the amount to the total.
    """
    total_income = 0
    for transaction in all_transactions:
        if transaction['type'] == 'income':
            total_income += transaction['amount']
    return total_income

def get_total_expenses():
    """
    This function calculates the total expenses.
    It iterates over all transactions, and for each transaction that is of type 'expense',
    it adds the amount to the total.
    """
    total_expenses = 0
    for transaction in all_transactions:
        if transaction['type'] == 'expense':
            total_expenses += transaction['amount']
    return total_expenses
