import sqlite3
import pandas as pd

from ratios import (
    calculate_net_profit_margin,
    calculate_operating_profit_margin,
    calculate_roe,
    calculate_roce,
    calculate_roa,
)

# Connect to database
conn = sqlite3.connect("nifty100.db")

# Read tables
pl = pd.read_sql("SELECT * FROM profitandloss", conn)
bs = pd.read_sql("SELECT * FROM balancesheet", conn)
sectors = pd.read_sql("SELECT * FROM sectors", conn)

# Merge Profit & Loss + Balance Sheet
df = pd.merge(
    pl,
    bs,
    on=["company_id", "year"],
    how="inner"
)

# Merge Sector Information
df = pd.merge(
    df,
    sectors[
        [
            "company_id",
            "broad_sector"
        ]
    ],
    on="company_id",
    how="left"
)

# -----------------------------------
# Calculate Ratios
# -----------------------------------

df["net_profit_margin_pct"] = df.apply(
    lambda x: calculate_net_profit_margin(
        x["net_profit"],
        x["sales"]
    ),
    axis=1
)

df["operating_profit_margin_pct"] = df.apply(
    lambda x: calculate_operating_profit_margin(
        x["operating_profit"],
        x["sales"]
    ),
    axis=1
)

df["return_on_equity_pct"] = df.apply(
    lambda x: calculate_roe(
        x["net_profit"],
        x["equity_capital"],
        x["reserves"]
    ),
    axis=1
)

df["return_on_capital_pct"] = df.apply(
    lambda x: calculate_roce(
        x["operating_profit"],
        x["equity_capital"],
        x["reserves"],
        x["borrowings"]
    ),
    axis=1
)

df["return_on_assets_pct"] = df.apply(
    lambda x: calculate_roa(
        x["net_profit"],
        x["total_assets"]
    ),
    axis=1
)

print("\n===== SAMPLE OUTPUT =====\n")

print(
    df[
        [
            "company_id",
            "year",
            "net_profit_margin_pct",
            "operating_profit_margin_pct",
            "return_on_equity_pct",
            "return_on_capital_pct",
            "return_on_assets_pct",
        ]
    ].head(10)
)

# -----------------------------------
# Financial Sector ROCE Benchmark
# -----------------------------------

df["roce_check"] = "Normal"

financial_mask = (
    df["broad_sector"] == "Financials"
)

df.loc[
    financial_mask,
    "roce_check"
] = "Financial Benchmark"

print("\n===== FINANCIAL SECTOR CHECK =====")
print("Financial Companies:", financial_mask.sum())

# -----------------------------------
# OPM Cross Check
# -----------------------------------

df["opm_difference"] = (
    df["operating_profit_margin_pct"] -
    df["opm_percentage"]
).abs()

opm_mismatch = df[
    df["opm_difference"] > 1
]

print("\n===== OPM MISMATCHS =====")
print("Mismatch Count:", len(opm_mismatch))

if len(opm_mismatch) > 0:

    opm_mismatch[
        [
            "company_id",
            "year",
            "operating_profit_margin_pct",
            "opm_percentage",
            "opm_difference"
        ]
    ].to_csv(
        "output/opm_mismatch.csv",
        index=False
    )

    print("output/opm_mismatch.csv generated successfully")

else:
    print("No mismatches found.")

conn.close()