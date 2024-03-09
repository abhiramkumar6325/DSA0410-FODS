import pandas as pd
import numpy as np
from scipy.stats import skew, kurtosis
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

data = {
    'Gene_ID': [1, 2, 3, 4, 5],
    'Tissue_Type_1': [10.2, 8.9, 11.5, 9.7, 8.3],
    'Tissue_Type_2': [9.8, 9.5, 12.0, 9.6, 8.7],
    'Tissue_Type_3': [8.5, 10.1, 10.8, 9.3, 9.0]
}

input_df = pd.DataFrame(data)

def asymmetry_measure(data):
    skewness = skew(data)
    kurt = kurtosis(data)
    asymmetry = abs(skewness) + abs(kurt)
    return asymmetry

asymmetry_scores = input_df.drop(columns='Gene_ID').apply(asymmetry_measure, axis=0)

data_transformed = np.log1p(input_df.drop(columns='Gene_ID'))  

kmeans = KMeans(n_clusters=3, random_state=42)
clusters_original = kmeans.fit_predict(input_df.drop(columns='Gene_ID'))
clusters_transformed = kmeans.fit_predict(data_transformed)

pca = PCA(n_components=2)
pca.fit(data_transformed)
transformed_pca = pca.transform(data_transformed)

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.scatter(transformed_pca[:, 0], transformed_pca[:, 1], c=clusters_original, cmap='viridis', alpha=0.5)
plt.title('Clustering on Original Data')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')

plt.subplot(1, 2, 2)
plt.scatter(transformed_pca[:, 0], transformed_pca[:, 1], c=clusters_transformed, cmap='viridis', alpha=0.5)
plt.title('Clustering on Transformed Data')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')

plt.tight_layout()
plt.show()

print("Asymmetry Scores:")
print(asymmetry_scores)
