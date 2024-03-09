import numpy as np
from scipy import stats

group_a_scores = [85, 78, 92, 89, 67, 76, 94, 82, 91, 88, 75, 81, 96, 90, 79, 83, 77, 85, 98, 72]
group_b_scores = [79, 86, 90, 73, 77, 81, 84, 88, 82, 75, 87, 80, 89, 91, 83, 85, 78, 92, 79, 81]

mean_group_a = np.mean(group_a_scores)
mean_group_b = np.mean(group_b_scores)

confidence_interval_group_a = stats.norm.interval(0.95, loc=mean_group_a, scale=stats.sem(group_a_scores))
confidence_interval_group_b = stats.norm.interval(0.95, loc=mean_group_b, scale=stats.sem(group_b_scores))

print("Group A:")
print("Mean Score:", mean_group_a)
print("95% Confidence Interval:", confidence_interval_group_a)
print("\nGroup B:")
print("Mean Score:", mean_group_b)
print("95% Confidence Interval:", confidence_interval_group_b)

t_statistic, p_value = stats.ttest_ind(group_a_scores, group_b_scores)
alpha = 0.05
print("\nHypothesis Test:")
print("Null Hypothesis: There is no significant difference between the two groups.")
print("Alternative Hypothesis: There is a significant difference between the two groups.")
print("Test Statistic:", t_statistic)
print("P-value:", p_value)

if p_value < alpha:
    print("Reject Null Hypothesis: There is a significant difference between the two groups.")
else:
    print("Fail to reject Null Hypothesis: There is no significant difference between the two groups.")
