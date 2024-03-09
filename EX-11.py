import pandas as pd
import matplotlib.pyplot as plt

weather_data = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
    'Temperature': [10, 12, 15, 18, 20],
    'Rainfall': [50, 40, 60, 30, 70]
})

fig, ax = plt.subplots()
ax.plot(weather_data['Month'], weather_data['Temperature'], marker='o', color='red', linestyle='-')
ax.set_xlabel('Month')
ax.set_ylabel('Temperature (°C)')
ax.set_title('Monthly Temperature Data (Line Plot)')
ax.grid(True)
plt.show()

fig, ax = plt.subplots()
ax.scatter(weather_data['Month'], weather_data['Rainfall'], color='blue')
ax.set_xlabel('Month')
ax.set_ylabel('Rainfall (mm)')
ax.set_title('Monthly Rainfall Data (Scatter Plot)')
ax.grid(True)
plt.show()
