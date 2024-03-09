import numpy as np
import matplotlib.pyplot as plt

likes_data = np.random.randint(1, 101, 100) 

likes_freq = np.bincount(likes_data)

plt.figure(figsize=(10, 6))
plt.bar(range(len(likes_freq)), likes_freq, color='skyblue')
plt.title('Frequency Distribution of Likes')
plt.xlabel('Number of Likes')
plt.ylabel('Frequency')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
