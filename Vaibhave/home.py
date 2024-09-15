import sqlite3
import bcrypt

# Connect to SQLite
conn = sqlite3.connect('finance.db')
cursor = conn.cursor()

def register_user(username, password, email):
    # Hash password
    password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    
    cursor.execute('INSERT INTO users (username, password_hash, email) VALUES (?, ?, ?)',
                   (username, password_hash, email))
    conn.commit()
    print(f"User {username} registered successfully.")

def login_user(username, password):
    cursor.execute('SELECT password_hash FROM users WHERE username = ?', (username,))
    result = cursor.fetchone()
    
    if result and bcrypt.checkpw(password.encode('utf-8'), result[0]):
        print(f"User {username} logged in successfully.")
    else:
        print("Invalid username or password.")
