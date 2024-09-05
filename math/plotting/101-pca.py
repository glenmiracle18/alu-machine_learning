#/usr/bin/env python3
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

# lib = np.load("pca.npz")
data = np.load('/data.npy')
labels = np.load('/labels.npy')

data_means = np.mean(data, axis=0)
norm_data = data - data_means
_, _, Vh = np.linalg.svd(norm_data)
pca_data = np.matmul(norm_data, Vh[:3].T)


fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(pca_data[:, 0] , pca_data[:, 1], pca_data[:, 2], c=
           labels, cmap='plasma',  s=40) #xs, ys, zx, c=markercolor, colormap, size
ax.set_title('PCA of Iris Dataset')
ax.set_xlabel('U1')
ax.set_ylabel('U22')
ax.set_zlabel('U3')
plt.show()
