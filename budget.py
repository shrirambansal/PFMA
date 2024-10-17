
import sqlite3
import main

# Connect to SQLlite database
conn = sqlite3.connect('finance.db')
c = conn.cursor()

def set_budget(user_id, category, budget_amount):
    c.execute("CREATE TABLE IF NOT EXISTS budgets (user_id INTEGER, category TEXT, amount REAL, PRIMARY KEY(user_id, category))")
    c.execute("REPLACE INTO budgets (user_id, category, amount) VALUES (?, ?, ?)", (user_id, category, budget_amount))
    conn.commit()
    print(f"Budget for {category} set at {budget_amount}")
    
    main.main2(id)

def check_budget(user_id):
    c.execute("SELECT category, amount FROM budgets WHERE user_id = ?", (user_id,))
    budgets = c.fetchall()

    for category, budget_amount in budgets:
        c.execute("SELECT SUM(amount) FROM transactions WHERE user_id = ? AND category = ? AND type = 'expense'", (user_id, category))
        spent = c.fetchone()[0] or 0
        if spent > budget_amount:
            print(f"Alert! You've exceeded your budget for {category}. Budget: {budget_amount}, Spent: {spent}")
        
            main.main2(id)
        else:
            print(f"Your budget for {category}. Budget: {budget_amount}, Spent: {spent}")
            
            main.main2(id)