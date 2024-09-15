def create_savings_goal(user_id, goal_name, target_amount):
    cursor.execute('INSERT INTO savings_goals (user_id, goal_name, target_amount, current_amount) VALUES (?, ?, ?, ?)',
                   (user_id, goal_name, target_amount, 0))
    conn.commit()
    print("Savings goal created successfully.")

def update_investment(user_id, investment_type, value):
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    cursor.execute('INSERT INTO investments (user_id, investment_type, value, date) VALUES (?, ?, ?, ?)',
                   (user_id, investment_type, value, date))
    conn.commit()
    print("Investment updated successfully.")
