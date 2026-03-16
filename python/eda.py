# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 12:38:59 2026

@author: halil
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 12:04:13 2026

@author: halil
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1) Veriyi oku
df = pd.read_csv("../data/ecommerce_transactions.csv")

print("İlk 5 satır:")
print(df.head())

print("\nVeri seti bilgisi:")
print(df.info())

print("\nSayısal özet:")
print(df.describe())

# 2) Kategorik dağılımlar
print("\nÜlke dağılımı:")
print(df["Country"].value_counts())

print("\nÜrün kategorisi dağılımı:")
print(df["Product_Category"].value_counts())

print("\nÖdeme yöntemi dağılımı:")
print(df["Payment_Method"].value_counts())

# 3) Temel grafikler
df["Product_Category"].value_counts().plot(kind="bar")
plt.title("Product Category Distribution")
plt.xlabel("Product Category")
plt.ylabel("Count")
plt.show()

df["Payment_Method"].value_counts().plot(kind="bar")
plt.title("Payment Method Distribution")
plt.xlabel("Payment Method")
plt.ylabel("Count")
plt.show()

# 4) Ortalama harcama analizleri
print("\nKategoriye göre ortalama harcama:")
print(df.groupby("Product_Category")["Purchase_Amount"].mean().sort_values(ascending=False))

print("\nÜlkeye göre ortalama harcama:")
print(df.groupby("Country")["Purchase_Amount"].mean().sort_values(ascending=False))

# 5) Yaş grupları
df["Age_Group"] = pd.cut(
    df["Age"],
    bins=[18, 25, 35, 45, 55, 65, 75],
    labels=["18-25", "26-35", "36-45", "46-55", "56-65", "65+"],
    include_lowest=True
)

print("\nYaş grubuna göre ortalama harcama:")
print(df.groupby("Age_Group", observed=False)["Purchase_Amount"].mean())

df.groupby("Age_Group", observed=False)["Purchase_Amount"].mean().plot(kind="bar")
plt.title("Average Spending by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Average Purchase Amount")
plt.show()

# 6) Tarih ve ay analizi
df["Transaction_Date"] = pd.to_datetime(df["Transaction_Date"])
df["Month"] = df["Transaction_Date"].dt.month

print("\nAya göre toplam satış hacmi:")
print(df.groupby("Month")["Purchase_Amount"].sum())

df.groupby("Month")["Purchase_Amount"].sum().plot(kind="line", marker="o")
plt.title("Monthly Sales Volume")
plt.xlabel("Month")
plt.ylabel("Total Purchase Amount")
plt.show()

# 7) Kategoriye göre toplam gelir
print("\nKategoriye göre toplam gelir:")
print(df.groupby("Product_Category")["Purchase_Amount"].sum().sort_values(ascending=False))

df.groupby("Product_Category")["Purchase_Amount"].sum().plot(kind="bar")
plt.title("Total Revenue by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Revenue")
plt.show()

# 8) Kategoriye göre ortalama harcama
print("\nKategoriye göre ortalama harcama (sıralı):")
print(df.groupby("Product_Category")["Purchase_Amount"].mean().sort_values(ascending=False))

# 9) Pivot table
pivot_table = pd.pivot_table(
    df,
    values="Purchase_Amount",
    index="Country",
    columns="Product_Category",
    aggfunc="sum"
)

print("\nCountry x Product Category Pivot Table:")
print(pivot_table)

# 10) Heatmap
plt.figure(figsize=(12, 6))
sns.heatmap(pivot_table, cmap="YlGnBu")
plt.title("Revenue Heatmap by Country and Category")
plt.xlabel("Product Category")
plt.ylabel("Country")
plt.show()