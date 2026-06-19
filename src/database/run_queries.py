import sqlite3
import pandas as pd

conn = sqlite3.connect("nifty100.db")

print("Total Companies")
print(pd.read_sql("SELECT COUNT(*) FROM companies", conn))

print("\nTop 10 Companies by Book Value")
print(pd.read_sql("""
SELECT company_name, book_value
FROM companies
ORDER BY book_value DESC
LIMIT 10
""", conn))

conn.close()