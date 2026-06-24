import sqlite3
import pandas as pd

conn = sqlite3.connect("nifty100.db")

tables = [
    "companies",
    "profitandloss",
    "balancesheet",
    "cashflow",
    "analysis",
    "documents",
    "prosandcons",
    "sectors",
    "stock_prices",
    "financial_ratios",
    "peer_groups"
]

for table in tables:
    count = pd.read_sql_query(
        f"SELECT COUNT(*) as cnt FROM {table}",
        conn
    )
    print(f"{table}: {count['cnt'][0]}")

conn.close()