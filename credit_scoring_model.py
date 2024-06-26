# -*- coding: utf-8 -*-
"""Credit Scoring Model.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1A9lzx-8484VEe3fazOQtPPZNFjgIpY_Y
"""

import pandas as pd

file_path = 'D:\Personal\Study\Task_1\Finance_data.csv'
data = pd.read_csv(file_path)

data.head()

data.columns

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np

# Create target variable
data['Credit_Score'] = data['Investment_Avenues'].apply(lambda x: 1 if x == 'Yes' else 0)
data.drop('Investment_Avenues', axis=1, inplace=True)

# Encode categorical variables
categorical_columns = data.select_dtypes(include=['object']).columns
data = pd.get_dummies(data, columns=categorical_columns, drop_first=True)

# Split the data into features and target variable
X = data.drop('Credit_Score', axis=1)
y = data['Credit_Score']

# Split the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the numerical features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

X_train[:5], y_train[:5]

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, roc_auc_score

# Initialize the Random Forest classifier
rf = RandomForestClassifier(random_state=42)

# Train the model
rf.fit(X_train, y_train)

# Make predictions
y_pred = rf.predict(X_test)
y_pred_proba = rf.predict_proba(X_test)[:, 1]

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
roc_auc = roc_auc_score(y_test, y_pred_proba)
classification_rep = classification_report(y_test, y_pred)

print(f'Accuracy: {accuracy}')
print(f'ROC-AUC: {roc_auc}')
print('Classification Report:')
print(classification_rep)