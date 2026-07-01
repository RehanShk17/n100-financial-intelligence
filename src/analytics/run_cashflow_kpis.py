import sqlite3
import pandas as pd

from cashflow_kpis import (
    calculate_free_cash_flow,
    calculate_cfo_quality_ratio,
    calculate_capex_intensity,
    calculate_fcf_conversion,
    classify_capital_allocation
)

# ----------------------------------------
# Connect Database
# ----------------------------------------

conn = sqlite3.connect("nifty100.db")

cashflow = pd.read_sql(
    "SELECT * FROM cashflow",
    conn
)

profit = pd.read_sql(
    "SELECT * FROM profitandloss",
    conn
)

# ----------------------------------------
# Merge Tables
# ----------------------------------------

df = pd.merge(
    cashflow,
    profit,
    on=["company_id", "year"],
    how="inner"
)

# ----------------------------------------
# Calculate KPIs
# ----------------------------------------

df["free_cash_flow"] = df.apply(
    lambda x: calculate_free_cash_flow(
        x["operating_activity"],
        x["investing_activity"]
    ),
    axis=1
)

df["cfo_quality_ratio"] = df.apply(
    lambda x: calculate_cfo_quality_ratio(
        x["operating_activity"],
        x["net_profit"]
    ),
    axis=1
)

df["capex_intensity"] = df.apply(
    lambda x: calculate_capex_intensity(
        x["investing_activity"],
        x["sales"]
    ),
    axis=1
)

df["fcf_conversion"] = df.apply(
    lambda x: calculate_fcf_conversion(
        x["free_cash_flow"],
        x["operating_profit"]
    ),
    axis=1
)

df["capital_allocation"] = df.apply(
    lambda x: classify_capital_allocation(
        x["operating_activity"],
        x["investing_activity"],
        x["financing_activity"]
    ),
    axis=1
)

# ----------------------------------------
# Display Sample
# ----------------------------------------

print("\n===== CASH FLOW KPI SAMPLE =====\n")

print(
    df[
        [
            "company_id",
            "year",
            "free_cash_flow",
            "cfo_quality_ratio",
            "capex_intensity",
            "fcf_conversion",
            "capital_allocation"
        ]
    ].head(10)
)

# ----------------------------------------
# Export CSV
# ----------------------------------------

df[
    [
        "company_id",
        "year",
        "free_cash_flow",
        "cfo_quality_ratio",
        "capex_intensity",
        "fcf_conversion",
        "capital_allocation"
    ]
].to_csv(
    "output/capital_allocation.csv",
    index=False
)

print("\noutput/capital_allocation.csv generated successfully")

conn.close()