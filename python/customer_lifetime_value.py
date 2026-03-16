# -*- coding: utf-8 -*-
"""
Customer Lifetime Value and Loyalty Analysis
"""

import pandas as pd

# 1) VERİYİ YÜKLE
df = pd.read_csv("../data/ecommerce_transactions.csv")

print("İlk 5 satır:")
print(df.head())

# 2) CUSTOMER LIFETIME VALUE (CLV)
clv = df.groupby("User_Name")["Purchase_Amount"].sum().reset_index()
clv.columns = ["Customer", "Customer_Lifetime_Value"]

top_customers = clv.sort_values(by="Customer_Lifetime_Value", ascending=False)

print("\nEn değerli 10 müşteri:")
print(top_customers.head(10))

print("\nOrtalama müşteri yaşam değeri:")
print(clv["Customer_Lifetime_Value"].mean())

# 3) CUSTOMER LOYALTY (SADAKAT)
loyalty = df.groupby("User_Name")["Transaction_ID"].count().reset_index()
loyalty.columns = ["Customer", "Purchase_Count"]

top_loyal_customers = loyalty.sort_values(by="Purchase_Count", ascending=False)

print("\nEn sadık 10 müşteri:")
print(top_loyal_customers.head(10))

print("\nOrtalama işlem sayısı:")
print(loyalty["Purchase_Count"].mean())

# 4) CLV + LOYALTY BİRLEŞTİR
customer_summary = pd.merge(clv, loyalty, on="Customer")

print("\nMüşteri özeti:")
print(customer_summary.head(10))

print("\nEn değerli ve sadık müşteriler:")
print(
    customer_summary.sort_values(
        by=["Customer_Lifetime_Value", "Purchase_Count"],
        ascending=False
    ).head(10)
)