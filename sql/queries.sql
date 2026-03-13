-- Ülkeye göre işlem sayısı
SELECT 
    Country,
    COUNT(*) AS transaction_count
FROM transactions
GROUP BY Country
ORDER BY transaction_count DESC;


-- Kategoriye göre toplam gelir
SELECT
    Product_Category,
    SUM(Purchase_Amount) AS total_revenue
FROM transactions
GROUP BY Product_Category
ORDER BY total_revenue DESC;


-- Ödeme yöntemine göre ortalama harcama
SELECT
    Payment_Method,
    AVG(Purchase_Amount) AS avg_purchase
FROM transactions
GROUP BY Payment_Method
ORDER BY avg_purchase DESC;


-- Aya göre satış trendi
SELECT
    strftime('%m', Transaction_Date) AS Month,
    SUM(Purchase_Amount) AS monthly_sales
FROM transactions
GROUP BY Month
ORDER BY Month;


-- Yaş grubuna göre ortalama harcama
SELECT
    CASE
        WHEN Age BETWEEN 18 AND 25 THEN '18-25'
        WHEN Age BETWEEN 26 AND 35 THEN '26-35'
        WHEN Age BETWEEN 36 AND 45 THEN '36-45'
        WHEN Age BETWEEN 46 AND 55 THEN '46-55'
        WHEN Age BETWEEN 56 AND 65 THEN '56-65'
        ELSE '65+'
    END AS Age_Group,
    AVG(Purchase_Amount) AS avg_purchase
FROM transactions
GROUP BY Age_Group
ORDER BY Age_Group;