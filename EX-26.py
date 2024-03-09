import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

data = {
    'id': [1, 2, 3, 4, 5],
    'name': ['Product A', 'Product B', 'Product C', 'Product D', 'Product E'],
    'brand': ['Brand X', 'Brand Y', 'Brand X', 'Brand Z', 'Brand X'],
    'categories': ['Electronics', 'Clothing', 'Electronics', 'Home', 'Electronics'],
    'manufacturer': ['Manufacturer 1', 'Manufacturer 2', 'Manufacturer 1', 'Manufacturer 3', 'Manufacturer 1'],
    'manufacturer Number': [123, 456, 789, 987, 654],
    'reviews date': ['2023-01-01', '2023-02-15', '2023-03-10', '2023-04-20', '2023-05-05'],
    'reviews id': [101, 102, 103, 104, 105],
    'reviews rating': [4.5, 3.8, 4.2, 4.0, 4.7],
    'reviews text': ['Great product!', 'Not satisfied.', 'Works well.', 'Average quality.', 'Highly recommended.']
}

df = pd.DataFrame(data)

sample_category = 'Electronics'

category_reviews = df[df['categories'] == sample_category]

if category_reviews.empty:
    print(f"No reviews found for the category '{sample_category}'")
else:
    mean_rating = category_reviews['reviews rating'].mean()
    sem = category_reviews['reviews rating'].sem()

    confidence_level = 0.95

    z_score = norm.ppf((1 + confidence_level) / 2)  # Two-tailed test
    margin_of_error = z_score * sem

    lower_bound = mean_rating - margin_of_error
    upper_bound = mean_rating + margin_of_error

    print(f"Average rating for {sample_category.capitalize()}: {mean_rating:.2f}")
    print(f"Confidence Interval ({confidence_level * 100}%): ({lower_bound:.2f}, {upper_bound:.2f})")

    plt.figure(figsize=(8, 6))
    plt.bar('Average Rating', mean_rating, yerr=margin_of_error, capsize=10, color='skyblue')
    plt.title(f"Confidence Interval for {sample_category.capitalize()} Rating")
    plt.ylabel("Rating")
    plt.xticks([])
    plt.grid(axis='y')
    plt.show()
