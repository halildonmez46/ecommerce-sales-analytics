# -*- coding: utf-8 -*-
"""
Machine Learning Model - High Spender Classification
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

#VERİYİ OKU

df = pd.read_csv("data/ecommerce_transactions.csv")

print("İlk 5 satır:")
print(df.head())

# 2) TARİHİ DÜZENLE


df["Transaction_Date"] = pd.to_datetime(df["Transaction_Date"])
df["Month"] = df["Transaction_Date"].dt.month


# 3) HIGH SPENDER LABEL OLUŞTUR


df["High_Spender"] = (df["Purchase_Amount"] > 500).astype(int)

print("\nHigh spender dağılımı:")
print(df["High_Spender"].value_counts())


# 4) KATEGORİK DEĞİŞKENLERİ ENCODE ET


le_country = LabelEncoder()
le_product = LabelEncoder()
le_payment = LabelEncoder()

df["Country"] = le_country.fit_transform(df["Country"])
df["Product_Category"] = le_product.fit_transform(df["Product_Category"])
df["Payment_Method"] = le_payment.fit_transform(df["Payment_Method"])

# 5) FEATURE VE TARGET AYIR


X = df[["Age","Country","Product_Category","Payment_Method","Month"]]
y = df["High_Spender"]

print("\nFeature örnekleri:")
print(X.head())


# 6) TRAIN TEST SPLIT


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("\nTrain size:", X_train.shape)
print("Test size:", X_test.shape)


# 7) MODEL

model = RandomForestClassifier(
    n_estimators=150,
    max_depth=10,
    random_state=42
)

model.fit(X_train, y_train)


# 8) TAHMİN

y_pred = model.predict(X_test)



# 9) MODEL PERFORMANSI


accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:", accuracy)

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))



# FEATURE IMPORTANCE


import matplotlib.pyplot as plt

importance = model.feature_importances_

features = X.columns

plt.bar(features, importance)

plt.title("Feature Importance")

plt.xlabel("Features")

plt.ylabel("Importance")

plt.show()