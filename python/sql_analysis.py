# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 12:43:12 2026

@author: halil
"""

import pandas as pd
import sqlite3

# Veritabanına bağlan
conn = sqlite3.connect("ecommerce.db")

# 1) Ülkeye göre işlem sayısı
query1 = """
SELECT Country, COUNT(*) AS transaction_count
FROM transactions
GROUP BY Country
ORDER BY transaction_count DESC
"""
result1 = pd.read_sql(query1, conn)

print("\n1) Ülkeye göre işlem sayısı:")
print(result1)

# 2) Kategoriye göre toplam gelir
query2 = """
SELECT Product_Category, SUM(Purchase_Amount) AS total_revenue
FROM transactions
GROUP BY Product_Category
ORDER BY total_revenue DESC
"""
result2 = pd.read_sql(query2, conn)

print("\n2) Kategoriye göre toplam gelir:")
print(result2)

# 3) Ödeme yöntemine göre ortalama harcama
query3 = """
SELECT Payment_Method, AVG(Purchase_Amount) AS avg_purchase
FROM transactions
GROUP BY Payment_Method
ORDER BY avg_purchase DESC
"""
result3 = pd.read_sql(query3, conn)

print("\n3) Ödeme yöntemine göre ortalama harcama:")
print(result3)

# 4) Aya göre toplam satış hacmi
query4 = """
SELECT Month, SUM(Purchase_Amount) AS monthly_sales
FROM transactions
GROUP BY Month
ORDER BY Month
"""
result4 = pd.read_sql(query4, conn)

print("\n4) Aya göre toplam satış hacmi:")
print(result4)

# 5) Yaş grubuna göre ortalama harcama
query5 = """
SELECT Age_Group, AVG(Purchase_Amount) AS avg_purchase
FROM transactions
GROUP BY Age_Group
ORDER BY Age_Group
"""
result5 = pd.read_sql(query5, conn)

print("\n5) Yaş grubuna göre ortalama harcama:")
print(result5)

# Bağlantıyı kapat
conn.close()