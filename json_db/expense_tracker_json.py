import json
import os

print('''============================
        Welcome to the Expense Tracker
         ============================''')

# JSON file
FILE_NAME = "expenses.json"


# ---------------- LOAD EXISTING DATA ----------------

if os.path.exists(FILE_NAME):

    with open(FILE_NAME, "r") as file:
        expensesList = json.load(file)

else:

    expensesList = []


# ---------------- MAIN PROGRAM ----------------

while True:

    print('''
======== MENU ========
1. Add Expense
2. View Expenses
3. View Total Expenses
4. Exit
5. Update Expense
6. Delete Expense
======================
''')

    choice = input("Enter your choice (1-6): ")


    # ==================================================
    # ADD EXPENSE
    # ==================================================

    if choice == "1":

        date = input("Enter the date: ")

        category = input(
            "Enter the category (food, travel, shopping, etc.): "
        )

        description = input(
            "Enter any other detail: "
        )

        amount = float(
            input("Enter the amount spent: ")
        )

        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        # Add expense to list
        expensesList.append(expense)

        # Save data to JSON
        with open(FILE_NAME, "w") as file:
            json.dump(expensesList, file, indent=4)

        print("\nExpense added successfully!")


    # ==================================================
    # VIEW EXPENSES
    # ==================================================

    elif choice == "2":

        if len(expensesList) == 0:

            print("\nNo expenses recorded yet.")

        else:

            print("\n========== YOUR EXPENSES ==========")

            count = 1

            for i in expensesList:

                print(
                    f"{count}. "
                    f"{i['date']} | "
                    f"{i['category']} | "
                    f"{i['description']} | "
                    f"₹{i['amount']}"
                )

                count += 1

            print("===================================")


    # ==================================================
    # VIEW TOTAL EXPENSES
    # ==================================================

    elif choice == "3":

        total = 0

        for i in expensesList:

            total += i["amount"]

        print(f"\nTotal Expenses: ₹{total}")


    # ==================================================
    # EXIT
    # ==================================================

    elif choice == "4":

        print("\nExiting the Expense Tracker.")
        print("Thank you!")

        break


    # ==================================================
    # UPDATE EXPENSE
    # ==================================================

    elif choice == "5":

        if len(expensesList) == 0:

            print("\nNo expenses available to update.")

        else:

            print("\n========== YOUR EXPENSES ==========")

            count = 1

            for i in expensesList:

                print(
                    f"{count}. "
                    f"{i['date']} | "
                    f"{i['category']} | "
                    f"{i['description']} | "
                    f"₹{i['amount']}"
                )

                count += 1

            print("===================================")

            expense_no = int(
                input("Enter the expense number you want to update: ")
            )

            # Check whether number is valid
            if expense_no < 1 or expense_no > len(expensesList):

                print("Invalid expense number.")

            else:

                # Convert expense number to list index
                index = expense_no - 1

                print("\nEnter the new details:")

                date = input("Enter new date: ")

                category = input(
                    "Enter new category: "
                )

                description = input(
                    "Enter new description: "
                )

                amount = float(
                    input("Enter new amount: ")
                )

                # Update the expense
                expensesList[index] = {
                    "date": date,
                    "category": category,
                    "description": description,
                    "amount": amount
                }

                # Save updated list to JSON
                with open(FILE_NAME, "w") as file:
                    json.dump(
                        expensesList,
                        file,
                        indent=4
                    )

                print("\nExpense updated successfully!")


    # ==================================================
    # DELETE EXPENSE
    # ==================================================

    elif choice == "6":

        if len(expensesList) == 0:

            print("\nNo expenses available to delete.")

        else:

            print("\n========== YOUR EXPENSES ==========")

            count = 1

            for i in expensesList:

                print(
                    f"{count}. "
                    f"{i['date']} | "
                    f"{i['category']} | "
                    f"{i['description']} | "
                    f"₹{i['amount']}"
                )

                count += 1

            print("===================================")

            expense_no = int(
                input("Enter the expense number you want to delete: ")
            )

            # Check whether number is valid
            if expense_no < 1 or expense_no > len(expensesList):

                print("Invalid expense number.")

            else:

                # Convert expense number to list index
                index = expense_no - 1

                # Remove expense
                deleted_expense = expensesList.pop(index)

                # Save updated list to JSON
                with open(FILE_NAME, "w") as file:
                    json.dump(
                        expensesList,
                        file,
                        indent=4
                    )

                print("\nExpense deleted successfully!")


    # ==================================================
    # INVALID CHOICE
    # ==================================================

    else:

        print("\nInvalid choice.")
        print("Please enter a number between 1 and 6.")