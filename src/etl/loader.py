import pandas as pd
from pathlib import Path

DATA_DIR = Path("data/raw")

files = [
    "companies.xlsx",
    "profitandloss.xlsx",
    "balancesheet.xlsx",
    "cashflow.xlsx",
    "analysis.xlsx",
    "documents.xlsx",
    "prosandcons.xlsx",
    "financial_ratios.xlsx",
    "market_cap.xlsx",
    "peer_groups.xlsx",
    "sectors.xlsx",
    "stock_prices.xlsx"
]

def load_excel(file_name):
    path = DATA_DIR / file_name

    try:
        df = pd.read_excel(path, skiprows=1)

        print("\n" + "=" * 50)
        print(file_name)
        print("=" * 50)
        print("Rows:", len(df))
        print("Columns:", len(df.columns))
        print("Headers:", list(df.columns))

        return df

    except Exception as e:
        print(f"Error loading {file_name}: {e}")

if __name__ == "__main__":
    for file in files:
        load_excel(file)