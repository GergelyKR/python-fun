# k-nearest neighbors
# Is the fruit an orange or a grapefruit?
# Put your object in a graph. The bigger, redder fruits are more likely grapefruits.
# Check the 3 nearest neighbors and see if they're orange or grapefruit
# More neighbors are oranges than grapefruit. So this fruit is probably an orange.
# This is using the k-nearest neighbors (KNN) algorithm for classification.
# This algorithm is used in many machine learning applications, including recommendation systems.
# - - -
# In the grapefruit example, you compared fruit based on how big they are and how red they are. Size and color are the features you’re comparing.
# Now suppose you have three fruit. You can extract the features. Then you can graph the three fruit.
# From the graph, you can tell visually that fruits A and B are similar. Let’s measure how close they are.
# To find the distance between two points, you use the Pythagorean formula: square root of (x2 - x1)2 + (y2 - y1)2
# When you have multiple points, instead of calculating the distance in two dimensions, you’re now calculating the distance in five dimensions, but the formula remains the same.

# Classification = categorization into a group
# Regression = predicting a response (like a number)

# Regression is very useful. Suppose you run a small bakery in Berkeley, and you make fresh bread every day. You’re trying to predict how many loaves to make for today.
# You have a set of features:
# • Weather on a scale of 1 to 5 (1 = bad, 5 = great).
# • Weekend or holiday? (1 if it’s a weekend or a holiday, 0 otherwise.)
# • Is there a game on? (1 if yes, 0 if no.)
# And you know how many loaves of bread you’ve sold in the past for different sets of features. You can use regression to predict how many loaves you should make.

# KNN is a really useful algorithm for machine learning and OCR for example.
# You can for example use it to compare common featuers of numbers, characters, faces, or frequently used words (for example in spam filtering)

from sklearn.neighbors import KNeighborsClassifier
import numpy as np

# Training data: [weight (g), diameter (cm)]
# 0 = Orange, 1 = Grapefruit
X_train = np.array([
    [150, 7],   # Orange
    [160, 7.5], # Orange
    [140, 6.8], # Orange
    [200, 8],   # Grapefruit
    [220, 8.5], # Grapefruit
    [210, 9]    # Grapefruit
])

y_train = np.array([0, 0, 0, 1, 1, 1])  # Labels

# Train KNN model
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

# Test case 1: closer to oranges
X_test1 = np.array([[170, 7.8]])
prediction1 = knn.predict(X_test1)

# Test case 2: bigger fruit, should be grapefruit
X_test2 = np.array([[210, 8.6]])
prediction2 = knn.predict(X_test2)

# Print results
print("Test fruit 1 (170g, 7.8cm):", "Orange 🍊" if prediction1[0] == 0 else "Grapefruit 🍊")
print("Test fruit 2 (210g, 8.6cm):", "Orange 🍊" if prediction2[0] == 0 else "Grapefruit 🍊")



# RECAP
# • KNN is used for classification and regression and involves looking at the k-nearest neighbors.
# • Classification = categorization into a group.
# • Regression = predicting a response (like a number).s
# • Feature extraction means converting an item (like a fruit or a user) into a list of numbers that can be compared.
# • Picking good features is an important part of a successful KNN algorithm.