# ---------------- EXPENSE TRACKER WITH FILE ----------------
'''
Expense tracker sending all data to the file
'''

expenses = []

def export_expenses(expenses):
    with open("expenses.txt", "w") as file:
        for expense in expenses:
            file.write(expense["name"] + " " + str(expense["amount"]) + "\n")
    print("Expenses exported successfully")


def main():
    while True:
        print("\n1. Add Expense")
        print("2. View Expenses")
        print("3. Export to File")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter expense name: ")
            amount = float(input("Enter amount: "))
            expenses.append({"name": name, "amount": amount})
            print("Expense added")

        elif choice == "2":
            if not expenses:
                print("No expenses found")
            else:
                for expense in expenses:
                    print(expense["name"], "-", expense["amount"])

        elif choice == "3":
            export_expenses(expenses)

        elif choice == "4":
            print("Exiting program")
            break

        else:
            print("Invalid choice, try again")


main()
