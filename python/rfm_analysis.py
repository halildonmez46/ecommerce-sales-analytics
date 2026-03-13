import pandas as pd

# VERİYİ YÜKLE
df = pd.read_csv("data/ecommerce_transactions.csv")

# tarih formatına çevir
df["Transaction_Date"] = pd.to_datetime(df["Transaction_Date"])

# ANALİZ TARİHİ
analysis_date = df["Transaction_Date"].max()

# RFM HESAPLAMA
rfm = df.groupby("User_Name").agg({
    "Transaction_Date": lambda x: (analysis_date - x.max()).days,
    "Transaction_ID": "count",
    "Purchase_Amount": "sum"
})

rfm.columns = ["Recency", "Frequency", "Monetary"]

print("\nRFM tablosu:")
print(rfm.head())


# RFM SKORLAMA

# Recency için rank kullanıyoruz, çünkü tekrar eden değerler çok
rfm["R_Score"] = pd.qcut(
    rfm["Recency"].rank(method="first"),
    4,
    labels=[4, 3, 2, 1]
)

rfm["F_Score"] = pd.qcut(
    rfm["Frequency"].rank(method="first"),
    4,
    labels=[1, 2, 3, 4]
)

rfm["M_Score"] = pd.qcut(
    rfm["Monetary"].rank(method="first"),
    4,
    labels=[1, 2, 3, 4]
)

rfm["RFM_Score"] = rfm["R_Score"].astype(str) + rfm["F_Score"].astype(str)

print("\nRFM skorları:")
print(rfm.head())


# SEGMENT OLUŞTURMA

def segment(row):
    score = row["RFM_Score"]

    if score in ["44", "43", "34"]:
        return "VIP Customers"
    elif score in ["33", "32", "42", "41"]:
        return "Loyal Customers"
    elif score in ["24", "23", "22", "31"]:
        return "Potential Customers"
    else:
        return "At Risk"

rfm["Customer_Segment"] = rfm.apply(segment, axis=1)

print("\nSegment dağılımı:")
print(rfm["Customer_Segment"].value_counts())

print("\nVIP müşteriler:")
print(rfm[rfm["Customer_Segment"] == "VIP Customers"].head(10))

print("\nSegment ortalamaları:")
print(
    rfm.groupby("Customer_Segment")[["Recency", "Frequency", "Monetary"]].mean()
)