import datetime
import sqlite3
import main

# Connect to SQLlite database
conn = sqlite3.connect('finance.db')
c = conn.cursor()

def add_transaction(user_id, amount, category, t_type):
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    c.execute("INSERT INTO transactions (user_id, amount, category, type, date) VALUES (?, ?, ?, ?, ?)", 
              (user_id, amount, category, t_type, date))
    conn.commit()
    print(f"{t_type.capitalize()} added successfully!")
    main.main2(id)

def view_transactions(user_id):
    c.execute("SELECT * FROM transactions WHERE user_id = ?", (user_id,))
    transactions = c.fetchall()


    print("\nTransactions:")
    for t in transactions:
        print(f"ID: {t[0]} | Amount: {t[2]} | Category: {t[3]} | Type: {t[4]} | Date: {t[5]}")


    main.main2(id)

def delete_transaction(transaction_id):
    c.execute("DELETE FROM transactions WHERE id = ?", (transaction_id,))
    conn.commit()
    print("Transaction deleted successfully!")
    main.main2(id)

def update_transaction(transaction_id, amount=None, category=None, t_type=None):
    # Fetch the existing transaction to ensure it exists
    c.execute("SELECT * FROM transactions WHERE id = ?", (transaction_id,))
    transaction = c.fetchone()
    
    if transaction:
        # If values are provided, use them, otherwise keep the existing values
        new_amount = amount if amount is not None else transaction[2]
        new_category = category if category is not None else transaction[3]
        new_t_type = t_type if t_type is not None else transaction[4]
        
        # Update the transaction with new values
        c.execute("UPDATE transactions SET amount = ?, category = ?, type = ? WHERE id = ?",
                  (new_amount, new_category, new_t_type, transaction_id))
        conn.commit()
        print("Transaction updated successfully!")
        main.main2(id)
    else:
        print("Transaction not found.")
        main.main2(id)
