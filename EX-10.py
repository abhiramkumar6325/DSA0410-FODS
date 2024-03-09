import pandas as pd
import matplotlib.pyplot as plt

sales_data = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
    'Sales': [10000, 12000, 15000, 11000, 13000]
})

fig, ax = plt.subplots()
ax.plot(sales_data['Month'], sales_data['Sales'], marker='o', color='blue', linestyle='-')
ax.set_xlabel('Month')
ax.set_ylabel('Sales')
ax.set_title('Monthly Sales Data (Line Plot)')
ax.grid(True)
plt.show()

fig, ax = plt.subplots()
ax.bar(sales_data['Month'], sales_data['Sales'], color='green')
ax.set_xlabel('Month')
ax.set_ylabel('Sales')
ax.set_title('Monthly Sales Data (Bar Plot)')
ax.grid(axis='y')
plt.show()
