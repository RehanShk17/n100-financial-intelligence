import sqlite3
import pandas as pd

from cagr import calculate_cagr

# Connect to database
conn = sqlite3.connect("nifty100.db")

# Read Profit & Loss table
pl = pd.read_sql(
    "SELECT * FROM profitandloss",
    conn
)

# Convert year to string for sorting
pl["year"] = pl["year"].astype(str)

results = []

# ---------------------------------------
# Process each company
# ---------------------------------------

for company in pl["company_id"].unique():

    company_df = (
        pl[pl["company_id"] == company]
        .sort_values("year")
        .reset_index(drop=True)
    )

    # ------------------------------
    # 3 Year CAGR
    # ------------------------------

    if len(company_df) >= 4:

        start3 = company_df.iloc[-4]
        end3 = company_df.iloc[-1]

        revenue_cagr_3, revenue_flag_3 = calculate_cagr(
            start3["sales"],
            end3["sales"],
            3
        )

        pat_cagr_3, pat_flag_3 = calculate_cagr(
            start3["net_profit"],
            end3["net_profit"],
            3
        )

        eps_cagr_3, eps_flag_3 = calculate_cagr(
            start3["eps"],
            end3["eps"],
            3
        )

    else:

        revenue_cagr_3 = None
        revenue_flag_3 = "INSUFFICIENT"

        pat_cagr_3 = None
        pat_flag_3 = "INSUFFICIENT"

        eps_cagr_3 = None
        eps_flag_3 = "INSUFFICIENT"

    # ------------------------------
    # 5 Year CAGR
    # ------------------------------

    if len(company_df) >= 6:

        start5 = company_df.iloc[-6]
        end5 = company_df.iloc[-1]

        revenue_cagr_5, revenue_flag_5 = calculate_cagr(
            start5["sales"],
            end5["sales"],
            5
        )

        pat_cagr_5, pat_flag_5 = calculate_cagr(
            start5["net_profit"],
            end5["net_profit"],
            5
        )

        eps_cagr_5, eps_flag_5 = calculate_cagr(
            start5["eps"],
            end5["eps"],
            5
        )

    else:

        revenue_cagr_5 = None
        revenue_flag_5 = "INSUFFICIENT"

        pat_cagr_5 = None
        pat_flag_5 = "INSUFFICIENT"

        eps_cagr_5 = None
        eps_flag_5 = "INSUFFICIENT"

    # ------------------------------
    # 10 Year CAGR
    # ------------------------------

    if len(company_df) >= 11:

        start10 = company_df.iloc[-11]
        end10 = company_df.iloc[-1]

        revenue_cagr_10, revenue_flag_10 = calculate_cagr(
            start10["sales"],
            end10["sales"],
            10
        )

        pat_cagr_10, pat_flag_10 = calculate_cagr(
            start10["net_profit"],
            end10["net_profit"],
            10
        )

        eps_cagr_10, eps_flag_10 = calculate_cagr(
            start10["eps"],
            end10["eps"],
            10
        )

    else:

        revenue_cagr_10 = None
        revenue_flag_10 = "INSUFFICIENT"

        pat_cagr_10 = None
        pat_flag_10 = "INSUFFICIENT"

        eps_cagr_10 = None
        eps_flag_10 = "INSUFFICIENT"

    # ---------------------------------------
    # Store Results
    # ---------------------------------------

    results.append({

        "company_id": company,

        # ---------------- 3 Year ----------------

        "revenue_cagr_3yr": revenue_cagr_3,
        "revenue_flag_3yr": revenue_flag_3,

        "pat_cagr_3yr": pat_cagr_3,
        "pat_flag_3yr": pat_flag_3,

        "eps_cagr_3yr": eps_cagr_3,
        "eps_flag_3yr": eps_flag_3,

        # ---------------- 5 Year ----------------

        "revenue_cagr_5yr": revenue_cagr_5,
        "revenue_flag_5yr": revenue_flag_5,

        "pat_cagr_5yr": pat_cagr_5,
        "pat_flag_5yr": pat_flag_5,

        "eps_cagr_5yr": eps_cagr_5,
        "eps_flag_5yr": eps_flag_5,

        # ---------------- 10 Year ----------------

        "revenue_cagr_10yr": revenue_cagr_10,
        "revenue_flag_10yr": revenue_flag_10,

        "pat_cagr_10yr": pat_cagr_10,
        "pat_flag_10yr": pat_flag_10,

        "eps_cagr_10yr": eps_cagr_10,
        "eps_flag_10yr": eps_flag_10,

    })

# ---------------------------------------
# Convert to DataFrame
# ---------------------------------------

results = pd.DataFrame(results)

print("\n===== CAGR SAMPLE OUTPUT =====\n")

print(results.head(10))

results.to_csv(
    "output/cagr_results.csv",
    index=False
)

print("\noutput/cagr_results.csv generated successfully")

conn.close()