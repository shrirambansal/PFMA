import datetime
import sqlite3
import main

# Connect to SQLlite database
conn = sqlite3.connect('finance.db')
c = conn.cursor()


def generate_report(user_id, period):
    if period == 1:#"monthly"
        date_filter = datetime.datetime.now().strftime("%Y-%m")
    elif period == 2:#"yearly"
        date_filter = datetime.datetime.now().strftime("%Y")

    c.execute(f"SELECT SUM(amount) FROM transactions WHERE user_id = ? AND type = 'income' AND date LIKE '{date_filter}%'", (user_id,))
    total_income = c.fetchone()[0] or 0

    c.execute(f"SELECT SUM(amount) FROM transactions WHERE user_id = ? AND type = 'expense' AND date LIKE '{date_filter}%'", (user_id,))
    total_expenses = c.fetchone()[0] or 0

    savings = total_income - total_expenses
    print(f"\nReport")
    print(f"Total Income: {total_income}")
    print(f"Total Expenses: {total_expenses}")
    print(f"Savings: {savings}")

    choice = int(input("Press 0 to Exit.... "))
    if(choice):
        
        main.main2(id)