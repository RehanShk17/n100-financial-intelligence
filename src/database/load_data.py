import sqlite3
import pandas as pd

conn = sqlite3.connect("nifty100.db")

# -------------------------
# Companies
# -------------------------
companies = pd.read_excel(
    "data/raw/companies.xlsx",
    skiprows=1
)

companies = companies[
    [
        "id",
        "company_name",
        "website",
        "face_value",
        "book_value",
        "roce_percentage",
        "roe_percentage"
    ]
]

companies.to_sql(
    "companies",
    conn,
    if_exists="append",
    index=False
)

print("Companies loaded!")

# -------------------------
# Profit & Loss
# -------------------------
profitandloss = pd.read_excel(
    "data/raw/profitandloss.xlsx",
    skiprows=1
)

profitandloss = profitandloss[
    [
        "id",
        "company_id",
        "year",
        "sales",
        "expenses",
        "operating_profit",
        "opm_percentage",
        "net_profit",
        "eps",
        "dividend_payout"
    ]
]

profitandloss.to_sql(
    "profitandloss",
    conn,
    if_exists="append",
    index=False
)

print("Profit & Loss loaded!")

# -------------------------
# Balance Sheet
# -------------------------
balancesheet = pd.read_excel(
    "data/raw/balancesheet.xlsx",
    skiprows=1
)

balancesheet = balancesheet[
    [
        "id",
        "company_id",
        "year",
        "equity_capital",
        "reserves",
        "borrowings",
        "total_liabilities",
        "total_assets"
    ]
]

balancesheet.to_sql(
    "balancesheet",
    conn,
    if_exists="append",
    index=False
)

print("Balance Sheet loaded!")

# -------------------------
# Cash Flow
# -------------------------
cashflow = pd.read_excel(
    "data/raw/cashflow.xlsx",
    skiprows=1
)

cashflow.to_sql(
    "cashflow",
    conn,
    if_exists="append",
    index=False
)

print("Cash Flow loaded!")

conn.close()

print("\nAll data loaded successfully!")