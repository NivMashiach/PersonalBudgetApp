from transactions import add_income, add_expense, delete_transaction, get_total_income, get_total_expenses, view_all_transactions

def view_current_balance():
    """
    This function calculates and displays the current balance.
    The balance is calculated by subtracting the total expenses from the total income.
    """
    total_income = get_total_income()
    total_expenses = get_total_expenses()
    current_balance = total_income - total_expenses
    print(f"Your current balance is: {current_balance}")

def display_menu():
    print("Welcome to Personal Budget App!")
    print("Please select an option:")
    print("1. Add income")
    print("2. Add expense")
    print("3. View current balance")
    print("4. View all transactions")
    print("5. Delete a transaction")
    print("6. Exit")

def get_user_choice():
    while True:  # Keep asking until user gives a valid input
        choice = input("Enter the number of your choice: ")
        if choice in ["1", "2", "3", "4", "5", "6"]:  # If user input is a valid option
            return choice  # Return the user's choice
        else:
            print("Invalid choice. Please choose a number between 1 and 6.")

def process_choice(choice):
    if choice == "1":
        add_income()
        ask_next_action()
    elif choice == "2":
        add_expense()
        ask_next_action()
    elif choice == "3":
        view_current_balance()
        ask_next_action()
    elif choice == "4":
        view_all_transactions()
        ask_next_action()
    elif choice == "5":
        delete_transaction()
        ask_next_action()
    elif choice == "6":
        print("Thank you for using Personal Budget App. Have a great day!")
        exit()
    else:
        print("Invalid choice. Please choose a valid option.")

def ask_next_action():
    while True:  # Keep asking until user gives a valid input
        print("\nQuick actions:")
        print("1. Add another income")
        print("2. Add another expense")
        print("3. View current balance")
        print("4. Return to main menu")
        print("5. Exit the program")

        choice = input("Choose an action: ")

        if choice in ["1", "2", "3", "4", "5"]:  # If user input is a valid option
            if choice == "1":
                add_income()
            elif choice == "2":
                add_expense()
            elif choice == "3":
                view_current_balance()
            elif choice == "4":
                return
            elif choice == "5":
                print("Thank you for using Personal Budget App. Have a great day!")
                exit()
            break  # Break the loop if a valid option was chosen
        else:
            print("Invalid choice. Please choose a number between 1 and 5.")
def main():
    while True:
        display_menu()
        choice = get_user_choice()
        process_choice(choice)

if __name__ == "__main__":
    main()
