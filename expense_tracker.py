import pandas as pd
import matplotlib.pyplot as plt

# Sample expense data
data = {
    'Category': ['Food','Rent','Entertainment','Bills','Transport'],
    'Amount': [500, 1200, 300, 250, 150]
}

df = pd.DataFrame(data)

# Print the table
print("✅ Monthly Expenses")
print(df)

# Bar chart: Expenses by category
plt.bar(df['Category'], df['Amount'], color='orange')
plt.title('Monthly Expenses by Category')
plt.xlabel('Category')
plt.ylabel('Amount ($)')
plt.show()

# Pie chart: Expense distribution
plt.pie(df['Amount'], labels=df['Category'], autopct='%1.1f%%', colors=['gold','lightblue','pink','lightgreen','violet'])
plt.title('Expense Distribution')
plt.show()
