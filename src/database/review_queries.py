import sqlite3
import pandas as pd

conn = sqlite3.connect("nifty100.db")

print("\n=== 5 Random Companies ===")
query = """
SELECT id, company_name
FROM companies
LIMIT 5
"""
print(pd.read_sql(query, conn))

print("\n=== Profit & Loss Coverage ===")
query = """
SELECT company_id,
       COUNT(*) AS years_available
FROM profitandloss
GROUP BY company_id
ORDER BY years_available DESC
LIMIT 10
"""
print(pd.read_sql(query, conn))

print("\n=== Balance Sheet Coverage ===")
query = """
SELECT company_id,
       COUNT(*) AS years_available
FROM balancesheet
GROUP BY company_id
ORDER BY years_available DESC
LIMIT 10
"""
print(pd.read_sql(query, conn))

print("\n=== Cash Flow Coverage ===")
query = """
SELECT company_id,
       COUNT(*) AS years_available
FROM cashflow
GROUP BY company_id
ORDER BY years_available DESC
LIMIT 10
"""
print(pd.read_sql(query, conn))

conn.close()