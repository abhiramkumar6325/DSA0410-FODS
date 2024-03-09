import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)
exam_scores = np.random.randint(40, 101, size=50)

plt.hist(exam_scores, bins=10, color='skyblue', edgecolor='black')

plt.xlabel('Exam Scores')
plt.ylabel('Frequency')
plt.title('Distribution of Exam Scores')

plt.show()
