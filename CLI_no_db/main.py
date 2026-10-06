
print('''============================
        Welcome to the Expense Tracker
         ============================''')

# list of all expenses (list of dictionaries)
expensesList = []

while True:

    print('''========MENU========
             1. Add Expense
             2. View Expenses
             3. View Total Expenses
             4. Update Expense
             5. Delete Expense
             6. Exit''')

    choice = int(input("Enter your choice (1-6): "))


    # ADD EXPENSE
    if choice == 1:

        date = input("Enter the date: ")
        category = input("Enter the category (food, travel, shopping, any other you want to enter): ")
        description = input("Any other detail you want to add: ")
        amount = float(input("Enter the amount spent: "))

        expense = {
            'date': date,
            'category': category,
            'description': description,
            'amount': amount
        }

        expensesList.append(expense)

        print("Expense added successfully!\nDone bro.")


    # VIEW EXPENSES
    elif choice == 2:

        if len(expensesList) == 0:

            print("No expenses recorded yet.")

        else:

            print("==== Your Expenses ====")

            count = 1

            for i in expensesList:

                print(
                    f"Expense no. {count} -> "
                    f"{i['date']} | "
                    f"{i['category']} | "
                    f"{i['description']} | "
                    f"{i['amount']}"
                )

                count += 1


    # VIEW TOTAL EXPENSES
    elif choice == 3:

        total = 0

        for i in expensesList:
            total += i['amount']

        print(f"Total Expenses: {total}")


    # UPDATE EXPENSE
    elif choice == 4:

        if len(expensesList) == 0:

            print("No expenses available to update.")

        else:

            print("==== Your Expenses ====")

            count = 1

            for i in expensesList:

                print(
                    f"Expense no. {count} -> "
                    f"{i['date']} | "
                    f"{i['category']} | "
                    f"{i['description']} | "
                    f"{i['amount']}"
                )

                count += 1

            expense_no = int(
                input("Enter the expense number you want to update: ")
            )

            if expense_no < 1 or expense_no > len(expensesList):

                print("Invalid expense number.")

            else:

                # Convert expense number into list index
                index = expense_no - 1

                print("Enter the new details:")

                date = input("Enter new date: ")
                category = input("Enter new category: ")
                description = input("Enter new description: ")
                amount = float(input("Enter new amount: "))

                expensesList[index] = {
                    'date': date,
                    'category': category,
                    'description': description,
                    'amount': amount
                }

                print("Expense updated successfully!")


    # DELETE EXPENSE
    elif choice == 5:

        if len(expensesList) == 0:

            print("No expenses available to delete.")

        else:

            print("==== Your Expenses ====")

            count = 1

            for i in expensesList:

                print(
                    f"Expense no. {count} -> "
                    f"{i['date']} | "
                    f"{i['category']} | "
                    f"{i['description']} | "
                    f"{i['amount']}"
                )

                count += 1

            expense_no = int(
                input("Enter the expense number you want to delete: ")
            )

            if expense_no < 1 or expense_no > len(expensesList):

                print("Invalid expense number.")

            else:

                # Convert expense number into list index
                index = expense_no - 1

                # Delete the expense
                deleted_expense = expensesList.pop(index)

                print("Expense deleted successfully!")


    # EXIT
    elif choice == 6:

        print("Exiting the Expense Tracker. Thank you!")

        break


    # INVALID CHOICE
    else:

        print("Invalid choice. Please enter a number between 1 and 6.")