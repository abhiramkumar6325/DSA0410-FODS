import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

control_group = np.array([82, 75, 68, 79, 80, 71, 74, 77, 72, 76])
treatment_group = np.array([86, 90, 82, 88, 92, 85, 87, 89, 84, 91])

t_statistic, p_value = ttest_ind(control_group, treatment_group)

plt.figure(figsize=(8, 6))
plt.boxplot([control_group, treatment_group], labels=['Control Group', 'Treatment Group'])
plt.title('Boxplot of Treatment Groups')
plt.ylabel('Treatment Effectiveness')
plt.xlabel('Group')
plt.grid(True)
plt.show()

print("Calculated p-value:", p_value)
if p_value < 0.05:
    print("The new treatment has a statistically significant effect.")
else:
    print("There is no statistically significant effect of the new treatment.")
