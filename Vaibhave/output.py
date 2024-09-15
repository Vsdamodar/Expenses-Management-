import pandas as pd
import matplotlib.pyplot as plt

def generate_report(user_id):
    income_df = pd.read_sql_query(f'SELECT * FROM income WHERE user_id = {user_id}', conn)
    expense_df = pd.read_sql_query(f'SELECT * FROM expenses WHERE user_id = {user_id}', conn)
    
    print(f"Income Report:\n{income_df}")
    print(f"Expense Report:\n{expense_df}")
    
    income_df['amount'].plot(kind='bar', title='Income Report')
    plt.show()
    
    expense_df['amount'].plot(kind='bar', title='Expense Report')
    plt.show()
