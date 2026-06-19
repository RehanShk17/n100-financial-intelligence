import sqlite3
import pandas as pd

conn = sqlite3.connect("nifty100.db")

tables = [
    "companies",
    "profitandloss",
    "balancesheet",
    "cashflow"
]

audit = []

for table in tables:

    count = pd.read_sql(
        f"SELECT COUNT(*) as row_count FROM {table}",
        conn
    )

    audit.append({
        "table": table,
        "row_count": int(count["row_count"][0])
    })

audit_df = pd.DataFrame(audit)

audit_df.to_csv(
    "output/load_audit.csv",
    index=False
)

print(audit_df)
print("\nload_audit.csv generated successfully!")

conn.close()