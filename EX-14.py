import numpy as np
import pandas as pd
from scipy.stats import skew, kurtosis
from sklearn.preprocessing import PowerTransformer
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

np.random.seed(0)
gene_expression_data = pd.DataFrame({
    'Tissue_Type': ['Tissue_A', 'Tissue_B', 'Tissue_C'],
    'Gene_1': np.random.normal(10, 2, 3),
    'Gene_2': np.random.normal(8, 3, 3),
    'Gene_3': np.random.normal(12, 1, 3)
})

skewness = skew(gene_expression_data.iloc[:, 1:])
kurt = kurtosis(gene_expression_data.iloc[:, 1:])

asymmetry_measure = skewness * np.sqrt(np.abs(kurt))

power_transformer = PowerTransformer(method='box-cox')
transformed_data = power_transformer.fit_transform(gene_expression_data.iloc[:, 1:])

kmeans_original = KMeans(n_clusters=3).fit(gene_expression_data.iloc[:, 1:])
kmeans_transformed = KMeans(n_clusters=3).fit(transformed_data)

pca_original = PCA(n_components=2).fit_transform(gene_expression_data.iloc[:, 1:])
pca_transformed = PCA(n_components=2).fit_transform(transformed_data)

