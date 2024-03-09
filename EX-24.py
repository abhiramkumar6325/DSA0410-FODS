import numpy as np
import scipy.stats as stats

design_A = [0, 1, 0, 1, 0, 1, 1, 0, 1, 0]
design_B = [1, 1, 0, 1, 1, 1, 0, 1, 1, 1]
mean_conversion_A = np.mean(design_A)
mean_conversion_B = np.mean(design_B)
print("Mean conversion rate for Design A:", mean_conversion_A)
print("Mean conversion rate for Design B:", mean_conversion_B)

t_statistic, p_value = stats.ttest_ind(design_A, design_B)

print("\nTwo-sample t-test results:")
print("Test Statistic:", t_statistic)
print("P-value:", p_value)

alpha = 0.05
if p_value < alpha:
    print("\nConclusion: Reject the null hypothesis. There is a statistically significant difference in the mean conversion rates between the two website designs.")
else:
    print("\nConclusion: Fail to reject the null hypothesis. There is no statistically significant difference in the mean conversion rates between the two website designs.")
