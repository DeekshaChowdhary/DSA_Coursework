# ---------------------- EXPENSE TRACKER ----------------------

"""
Features:
- Add Expense
- View Expenses
- Exit

Note:
- Stores multiple expenses using list of dictionaries
"""


# ---------------------- DATA ----------------------
expenses = []


# ---------------------- FUNCTIONS ----------------------

def add_expense():
    """Add a new expense"""
    name = input("Enter expense name: ")
    amount = float(input("Enter expense amount: "))

    expense = {
        "name": name,
        "amount": amount
    }

    expenses.append(expense)
    print("Expense added successfully")


def view_expenses():
    """Display all expenses"""
    if not expenses:
        print("No expenses found")
    else:
        print("\n------ Expense List ------")
        total = 0

        for exp in expenses:
            print(exp["name"], "-", exp["amount"])
            total += exp["amount"]

        print("--------------------------")
        print("Total Expense:", total)


def show_menu():
    """Display menu"""
    print("\n------ Expense Tracker ------")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")


# ---------------------- MAIN PROGRAM ----------------------

def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            print("Exiting program...")
            break

        else:
            print("Invalid choice, try again")


# ---------------------- RUN ----------------------
if __name__ == "__main__":
    main()
