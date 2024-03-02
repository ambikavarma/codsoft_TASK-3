# -*- coding: utf-8 -*-
"""IRIS FLOWER CLASSIFICATION

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VbLfr9XXh09fkYTcaQ3SGZm5jCM3JFkB
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
data = pd.read_csv("IRIS.csv")

data.head()

data.isnull().sum()

###no null values

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score, precision_score, recall_score, f1_score

X = data[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
y = data['species']

# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalizing the features using StandardScaler
scaler = StandardScaler()
X_train_normalized = scaler.fit_transform(X_train)
X_test_normalized = scaler.transform(X_test)

pipeline = Pipeline([
    ('svc', SVC(kernel='linear'))
])

pipeline.fit(X_train_normalized, y_train)

y_pred = pipeline.predict(X_test_normalized)

# Evaluating the model
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average="micro")
recall = recall_score(y_test, y_pred, average="micro")
f1 = f1_score(y_test, y_pred, average="micro")

print("Precision", precision)
print("Recall", recall)
print("f1_score", f1)
print("Accuracy:", accuracy)
print("Classification Report:")
print(classification_report(y_test, y_pred))

# Find indices where predictions match true labels
correct_indices = np.where(y_pred == y_test)[0]

# Print indices of correct predictions
print("Indices of correctly classified Iris flowers:")
print(correct_indices)