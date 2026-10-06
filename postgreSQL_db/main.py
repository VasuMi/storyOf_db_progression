import psycopg


# ==================================================
# CONNECT TO POSTGRESQL
# ==================================================

connection = psycopg.connect(
    host="localhost",
    port=5432,
    dbname="expense_tracker",
    user="postgres",
    password="YOUR_POSTGRES_PASSWORD"
)

cursor = connection.cursor()


# ==================================================
# CREATE TABLE
# ==================================================

cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id SERIAL PRIMARY KEY,
        date TEXT NOT NULL,
        category TEXT NOT NULL,
        description TEXT,
        amount NUMERIC(10, 2) NOT NULL
    )
""")

connection.commit()


# ==================================================
# WELCOME
# ==================================================

print('''============================
        Welcome to the Expense Tracker
         ============================''')


# ==================================================
# MAIN PROGRAM
# ==================================================

while True:

    print('''========MENU========
             1. Add Expense
             2. View Expenses
             3. View Total Expenses
             4. Update Expense
             5. Delete Expense
             6. Exit''')

    choice = int(input("Enter your choice (1-6): "))


    # ==================================================
    # ADD EXPENSE
    # ==================================================

    if choice == 1:

        date = input("Enter the date: ")

        category = input(
            "Enter the category "
            "(food, travel, shopping, any other you want to enter): "
        )

        description = input(
            "Any other detail you want to add: "
        )

        amount = float(
            input("Enter the amount spent: ")
        )


        cursor.execute("""
            INSERT INTO expenses
            (date, category, description, amount)
            VALUES (%s, %s, %s, %s)
        """, (date, category, description, amount))


        connection.commit()


        print("Expense added successfully!\nDone bro.")


    # ==================================================
    # VIEW EXPENSES
    # ==================================================

    elif choice == 2:

        cursor.execute("""
            SELECT id, date, category, description, amount
            FROM expenses
            ORDER BY id
        """)

        expenses = cursor.fetchall()


        if len(expenses) == 0:

            print("No expenses recorded yet.")

        else:

            print("==== Your Expenses ====")


            for expense in expenses:

                print(
                    f"Expense ID: {expense[0]} -> "
                    f"{expense[1]} | "
                    f"{expense[2]} | "
                    f"{expense[3]} | "
                    f"₹{expense[4]}"
                )


    # ==================================================
    # VIEW TOTAL EXPENSES
    # ==================================================

    elif choice == 3:

        cursor.execute("""
            SELECT COALESCE(SUM(amount), 0)
            FROM expenses
        """)

        total = cursor.fetchone()[0]


        print(f"Total Expenses: ₹{total}")


    # ==================================================
    # UPDATE EXPENSE
    # ==================================================

    elif choice == 4:

        cursor.execute("""
            SELECT id, date, category, description, amount
            FROM expenses
            ORDER BY id
        """)

        expenses = cursor.fetchall()


        if len(expenses) == 0:

            print("No expenses available to update.")

        else:

            print("==== Your Expenses ====")


            for expense in expenses:

                print(
                    f"Expense ID: {expense[0]} -> "
                    f"{expense[1]} | "
                    f"{expense[2]} | "
                    f"{expense[3]} | "
                    f"₹{expense[4]}"
                )


            expense_id = int(
                input("Enter the expense ID you want to update: ")
            )


            # Check if expense exists

            cursor.execute("""
                SELECT id
                FROM expenses
                WHERE id = %s
            """, (expense_id,))


            expense = cursor.fetchone()


            if expense is None:

                print("Invalid expense ID.")

            else:

                print("Enter the new details:")

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
                    SET date = %s,
                        category = %s,
                        description = %s,
                        amount = %s
                    WHERE id = %s
                """,
                (
                    date,
                    category,
                    description,
                    amount,
                    expense_id
                ))


                connection.commit()


                print("Expense updated successfully!")


    # ==================================================
    # DELETE EXPENSE
    # ==================================================

    elif choice == 5:

        cursor.execute("""
            SELECT id, date, category, description, amount
            FROM expenses
            ORDER BY id
        """)

        expenses = cursor.fetchall()


        if len(expenses) == 0:

            print("No expenses available to delete.")

        else:

            print("==== Your Expenses ====")


            for expense in expenses:

                print(
                    f"Expense ID: {expense[0]} -> "
                    f"{expense[1]} | "
                    f"{expense[2]} | "
                    f"{expense[3]} | "
                    f"₹{expense[4]}"
                )


            expense_id = int(
                input("Enter the expense ID you want to delete: ")
            )


            # Check if expense exists

            cursor.execute("""
                SELECT id
                FROM expenses
                WHERE id = %s
            """, (expense_id,))


            expense = cursor.fetchone()


            if expense is None:

                print("Invalid expense ID.")

            else:

                confirm = input(
                    "Are you sure you want to delete this expense? (y/n): "
                )


                if confirm.lower() == "y":

                    cursor.execute("""
                        DELETE FROM expenses
                        WHERE id = %s
                    """, (expense_id,))


                    connection.commit()


                    print("Expense deleted successfully!")

                else:

                    print("Deletion cancelled.")


    # ==================================================
    # EXIT
    # ==================================================

    elif choice == 6:

        print("Exiting the Expense Tracker. Thank you!")

        break


    # ==================================================
    # INVALID CHOICE
    # ==================================================

    else:

        print("Invalid choice. Please enter a number between 1 and 6.")


# ==================================================
# CLOSE DATABASE
# ==================================================

cursor.close()
connection.close()
