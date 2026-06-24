import pandas as pd
import sqlite3

conn = sqlite3.connect("nifty100.db")

# Companies
companies = pd.read_excel("data/raw/companies.xlsx", skiprows=1)
companies.columns = [
    "id","company_logo","company_name","chart_link",
    "about_company","website","nse_profile","bse_profile",
    "face_value","book_value","roce_percentage","roe_percentage"
]
companies.to_sql("companies", conn, if_exists="append", index=False)
print("Companies loaded!")

# Profit & Loss
profitandloss = pd.read_excel("data/raw/profitandloss.xlsx", skiprows=1)
profitandloss.to_sql("profitandloss", conn, if_exists="append", index=False)
print("Profit & Loss loaded!")

# Balance Sheet
balancesheet = pd.read_excel("data/raw/balancesheet.xlsx", skiprows=1)
balancesheet.to_sql("balancesheet", conn, if_exists="append", index=False)
print("Balance Sheet loaded!")

# Cash Flow
cashflow = pd.read_excel("data/raw/cashflow.xlsx", skiprows=1)
cashflow.to_sql("cashflow", conn, if_exists="append", index=False)
print("Cash Flow loaded!")

# Analysis
analysis = pd.read_excel("data/raw/analysis.xlsx", skiprows=1)
analysis.to_sql("analysis", conn, if_exists="append", index=False)
print("Analysis loaded!")

# Documents
documents = pd.read_excel("data/raw/documents.xlsx", skiprows=1)
documents.columns = ["id","company_id","year","annual_report"]
documents.to_sql("documents", conn, if_exists="append", index=False)
print("Documents loaded!")

# Pros and Cons
prosandcons = pd.read_excel("data/raw/prosandcons.xlsx", skiprows=1)
prosandcons.to_sql("prosandcons", conn, if_exists="append", index=False)
print("Pros & Cons loaded!")

# Sectors
sectors = pd.read_excel("data/raw/sectors.xlsx")
sectors.to_sql("sectors", conn, if_exists="append", index=False)
print("Sectors loaded!")

# Stock Prices
stock_prices = pd.read_excel("data/raw/stock_prices.xlsx")
stock_prices.to_sql("stock_prices", conn, if_exists="append", index=False)
print("Stock Prices loaded!")

# Financial Ratios
financial_ratios = pd.read_excel("data/raw/financial_ratios.xlsx")
financial_ratios.to_sql("financial_ratios", conn, if_exists="append", index=False)
print("Financial Ratios loaded!")

# Peer Groups
peer_groups = pd.read_excel("data/raw/peer_groups.xlsx")
peer_groups.to_sql("peer_groups", conn, if_exists="append", index=False)
print("Peer Groups loaded!")

conn.close()

print("\nAll 11 tables loaded successfully!")