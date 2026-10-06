
import sqlite3


# ==================================================
# DATABASE CONNECTION
# ==================================================

connection = sqlite3.connect("expenses.db")

cursor = connection.cursor()


# ==================================================
# CREATE TABLE
# ==================================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    category TEXT NOT NULL,
    description TEXT,
    amount REAL NOT NULL
)
""")

connection.commit()


print('''============================
        Welcome to the Expense Tracker
         ============================''')


# ==================================================
# MAIN PROGRAM
# ==================================================

while True:

    print('''
======== MENU ========
1. Add Expense
2. View Expenses
3. View Total Expenses
4. Update Expense
5. Delete Expense
6. Exit
======================
''')

    choice = int(input("Enter your choice (1-6): "))


    # ==================================================
    # ADD EXPENSE
    # ==================================================

    if choice == 1:

        date = input("Enter the date: ")

        category = input(
            "Enter the category (food, travel, shopping, etc.): "
        )

        description = input(
            "Any other detail you want to add: "
        )

        amount = float(
            input("Enter the amount spent: ")
        )


        cursor.execute("""
        INSERT INTO expenses (date, category, description, amount)
        VALUES (?, ?, ?, ?)
        """, (date, category, description, amount))


        connection.commit()


        print("\nExpense added successfully!")


    # ==================================================
    # VIEW EXPENSES
    # ==================================================

    elif choice == 2:

        cursor.execute("""
        SELECT * FROM expenses
        """)

        expenses = cursor.fetchall()


        if len(expenses) == 0:

            print("\nNo expenses recorded yet.")

        else:

            print("\n========== YOUR EXPENSES ==========")


            for expense in expenses:

                print(
                    f"ID: {expense[0]} | "
                    f"Date: {expense[1]} | "
                    f"Category: {expense[2]} | "
                    f"Description: {expense[3]} | "
                    f"Amount: ₹{expense[4]}"
                )


            print("===================================")


    # ==================================================
    # VIEW TOTAL EXPENSES
    # ==================================================

    elif choice == 3:

        cursor.execute("""
        SELECT SUM(amount) FROM expenses
        """)

        total = cursor.fetchone()[0]


        if total is None:
            total = 0


        print(f"\nTotal Expenses: ₹{total}")


    # ==================================================
    # UPDATE EXPENSE
    # ==================================================

    elif choice == 4:

        cursor.execute("""
        SELECT * FROM expenses
        """)

        expenses = cursor.fetchall()


        if len(expenses) == 0:

            print("\nNo expenses available to update.")

        else:

            print("\n========== YOUR EXPENSES ==========")


            for expense in expenses:

                print(
                    f"ID: {expense[0]} | "
                    f"{expense[1]} | "
                    f"{expense[2]} | "
                    f"{expense[3]} | "
                    f"₹{expense[4]}"
                )


            expense_id = int(
                input("\nEnter the ID of the expense you want to update: ")
            )


            # Check whether expense exists

            cursor.execute("""
            SELECT * FROM expenses
            WHERE id = ?
            """, (expense_id,))


            expense = cursor.fetchone()


            if expense is None:

                print("Invalid expense ID.")

            else:

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


                cursor.execute("""
                UPDATE expenses
                SET date = ?,
                    category = ?,
                    description = ?,
                    amount = ?
                WHERE id = ?
                """,
                (
                    date,
                    category,
                    description,
                    amount,
                    expense_id
                ))


                connection.commit()


                print("\nExpense updated successfully!")


    # ==================================================
    # DELETE EXPENSE
    # ==================================================

    elif choice == 5:

        cursor.execute("""
        SELECT * FROM expenses
        """)

        expenses = cursor.fetchall()


        if len(expenses) == 0:

            print("\nNo expenses available to delete.")

        else:

            print("\n========== YOUR EXPENSES ==========")


            for expense in expenses:

                print(
                    f"ID: {expense[0]} | "
                    f"{expense[1]} | "
                    f"{expense[2]} | "
                    f"{expense[3]} | "
                    f"₹{expense[4]}"
                )


            expense_id = int(
                input("\nEnter the ID of the expense you want to delete: ")
            )


            # Check whether expense exists

            cursor.execute("""
            SELECT * FROM expenses
            WHERE id = ?
            """, (expense_id,))


            expense = cursor.fetchone()


            if expense is None:

                print("Invalid expense ID.")

            else:

                # Confirm deletion

                confirm = input(
                    "Are you sure you want to delete this expense? (y/n): "
                )


                if confirm.lower() == "y":

                    cursor.execute("""
                    DELETE FROM expenses
                    WHERE id = ?
                    """, (expense_id,))


                    connection.commit()


                    print("\nExpense deleted successfully!")

                else:

                    print("\nDeletion cancelled.")


    # ==================================================
    # EXIT
    # ==================================================

    elif choice == 6:

        print("\nExiting the Expense Tracker.")
        print("Thank you!")

        break


    # ==================================================
    # INVALID CHOICE
    # ==================================================

    else:

        print("\nInvalid choice.")
        print("Please enter a number between 1 and 6.")


# ==================================================
# CLOSE DATABASE CONNECTION
# ==================================================

connection.close()
