# ---------------------------------
# 1. KMEANS CLUSTERING
# ---------------------------------

from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

print("----- KMEANS CLUSTERING -----")

# Sample dataset
X_cluster = np.array([
    [2, 3],
    [3, 4],
    [2, 2],
    [8, 7],
    [9, 8],
    [8, 9]
])

# Create KMeans model
kmeans = KMeans(n_clusters=2, random_state=42)

# Train model
kmeans.fit(X_cluster)

# Results
print("Cluster Labels:", kmeans.labels_)
print("Centroids:\n", kmeans.cluster_centers_)

# Visualization
plt.scatter(X_cluster[:, 0], X_cluster[:, 1], c=kmeans.labels_, cmap='viridis')
plt.scatter(kmeans.cluster_centers_[:, 0],
            kmeans.cluster_centers_[:, 1],
            s=200, c='red', marker='X')
plt.title("KMeans Clustering")
plt.show()


# ---------------------------------
# 2. KNN CLASSIFICATION
# ---------------------------------

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

print("\n----- KNN CLASSIFICATION -----")

# Load dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Scale features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Create model
knn_classifier = KNeighborsClassifier(n_neighbors=5)

# Train
knn_classifier.fit(X_train, y_train)

# Predict
y_pred = knn_classifier.predict(X_test)

# Accuracy
print("Classification Accuracy:", accuracy_score(y_test, y_pred))


# ---------------------------------
# 3. KNN REGRESSION
# ---------------------------------

from sklearn.neighbors import KNeighborsRegressor

print("\n----- KNN REGRESSION -----")

# Training data
X_reg = np.array([[1], [2], [3], [4], [5]])   # Hours studied
y_reg = np.array([30, 45, 50, 65, 85])        # Marks scored

# Create model
knn_regressor = KNeighborsRegressor(n_neighbors=3)

# Train
knn_regressor.fit(X_reg, y_reg)

# Predict for new value
new_hours = [[3.5]]
predicted_score = knn_regressor.predict(new_hours)

print("Predicted Score for 3.5 hours study:", predicted_score[0])