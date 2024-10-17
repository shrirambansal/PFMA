import sqlite3
import getpass
import main

# Connect to SQLlite database
conn = sqlite3.connect('finance.db')
c = conn.cursor()

# Create tables for users and transactions
c.execute('''CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE,
                password TEXT
            )''')

c.execute('''CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                amount REAL,
                category TEXT,
                type TEXT,  -- 'income' or 'expense'
                date TEXT,
                FOREIGN KEY(user_id) REFERENCES users(id)
            )''')

conn.commit()

def register():
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")

    try:
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        print("User registered successfully!")
        main.main()
    except sqlite3.IntegrityError:
        print("Username already exists!")
        register()

def login():
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")

    c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = c.fetchone()

    if user:
        print("*"*50)
        print(f"Welcome back, {username} - {user[0]}!")
        # Return user id for future actions
        return user[0]  
    else:
        print("Invalid credentials!")
        login()