import datetime

def add_income(user_id, category, amount):
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    cursor.execute('INSERT INTO income (user_id, category, amount, date) VALUES (?, ?, ?, ?)',
                   (user_id, category, amount, date))
    conn.commit()
    print("Income added successfully.")

def add_expense(user_id, category, amount):
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    cursor.execute('INSERT INTO expenses (user_id, category, amount, date) VALUES (?, ?, ?, ?)',
                   (user_id, category, amount, date))
    conn.commit()
    print("Expense added successfully.")
