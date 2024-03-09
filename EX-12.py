import pandas as pd
import matplotlib.pyplot as plt

sales_data = pd.DataFrame({
    'Date': ['2022-01-01', '2022-02-01', '2022-03-01', '2022-04-01', '2022-05-01'],
    'Sales': [10000, 12000, 15000, 18000, 20000]
})

sales_data['Date'] = pd.to_datetime(sales_data['Date'])

plt.figure(figsize=(10, 5))
plt.plot(sales_data['Date'], sales_data['Sales'], marker='o', color='skyblue', linestyle='-')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.title('Sales Over Time (Line Plot)')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 5))
plt.scatter(sales_data['Date'], sales_data['Sales'], color='green')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.title('Sales Over Time (Scatter Plot)')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
