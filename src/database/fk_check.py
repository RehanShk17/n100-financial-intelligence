import sqlite3
import pandas as pd

conn = sqlite3.connect("nifty100.db")

query = """
SELECT COUNT(*)
FROM profitandloss p
LEFT JOIN companies c
ON p.company_id = c.id
WHERE c.id IS NULL
"""

print("Invalid Company References:")
print(pd.read_sql(query, conn))

conn.close()