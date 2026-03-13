# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 12:39:26 2026

@author: halil
"""

import pandas as pd
import sqlite3

# Veriyi oku
df = pd.read_csv("data/ecommerce_transactions.csv")

# Tarih kolonunu datetime yap
df["Transaction_Date"] = pd.to_datetime(df["Transaction_Date"])

# Ay bilgisini ekle
df["Month"] = df["Transaction_Date"].dt.month

# Yaş grubu ekle
df["Age_Group"] = pd.cut(
    df["Age"],
    bins=[18, 25, 35, 45, 55, 65, 75],
    labels=["18-25", "26-35", "36-45", "46-55", "56-65", "65+"],
    include_lowest=True
)

# SQLite veritabanına bağlan
conn = sqlite3.connect("ecommerce.db")

# DataFrame'i SQL tablosuna yaz
df.to_sql("transactions", conn, if_exists="replace", index=False)

print("Veri başarıyla SQL veritabanına aktarıldı.")

# Kontrol sorgusu
query = "SELECT COUNT(*) AS total_rows FROM transactions"
result = pd.read_sql(query, conn)

print(result)

conn.close()