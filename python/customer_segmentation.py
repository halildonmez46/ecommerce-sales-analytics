# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 14:29:47 2026

@author: halil
"""

# Customer Segmentation with K-Means

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.cluster import KMeans

# 1) DATA LOAD

df = pd.read_csv("../data/ecommerce_transactions.csv")

# 2) FEATURE HAZIRLA

df["Transaction_Date"] = pd.to_datetime(df["Transaction_Date"])
df["Month"] = df["Transaction_Date"].dt.month

le_country = LabelEncoder()
le_product = LabelEncoder()

df["Country"] = le_country.fit_transform(df["Country"])
df["Product_Category"] = le_product.fit_transform(df["Product_Category"])

# clustering için basit feature set
X = df[["Age","Country","Product_Category","Purchase_Amount"]]

print("Feature örnekleri:")
print(X.head())

# 3) K-MEANS MODELİ

kmeans = KMeans(n_clusters=4, random_state=42)

df["Customer_Segment"] = kmeans.fit_predict(X)

print("\nSegment dağılımı:")
print(df["Customer_Segment"].value_counts())

# 4) SEGMENT ANALİZİ

segment_summary = df.groupby("Customer_Segment")[["Age","Purchase_Amount"]].mean()

print("\nSegment ortalamaları:")
print(segment_summary)

# 5) GRAFİK

plt.figure(figsize=(8,6))

plt.scatter(
    df["Age"],
    df["Purchase_Amount"],
    c=df["Customer_Segment"],
    cmap="viridis",
    alpha=0.5
)

plt.xlabel("Age")
plt.ylabel("Purchase Amount")
plt.title("Customer Segments")

plt.show()