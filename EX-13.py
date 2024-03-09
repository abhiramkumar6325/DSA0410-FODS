import pandas as pd
from scipy.stats import skew, kurtosis

data = {
    'Numeric_Column': [10, 15, 20, 25, 30],
    'Categorical_Column': ['A', 'B', 'A', 'C', 'B']
}

df = pd.DataFrame(data)

mean_numeric = df['Numeric_Column'].mean()
variance_numeric = df['Numeric_Column'].var()
skewness_numeric = skew(df['Numeric_Column'])
kurtosis_numeric = kurtosis(df['Numeric_Column'])

print("Statistical Measures for Numeric Column:")
print("Mean:", mean_numeric)
print("Variance:", variance_numeric)
print("Skewness:", skewness_numeric)
print("Kurtosis:", kurtosis_numeric)

outliers = df[(df['Numeric_Column'] < mean_numeric - 2 * variance_numeric) | (df['Numeric_Column'] > mean_numeric + 2 * variance_numeric)]

print("\nOutliers:")
print(outliers)

