import pandas as pd

print("\n==============================")
print("DATA QUALITY CHECKS (DQ-01 to DQ-16)")
print("==============================")

# Load files
companies = pd.read_excel("data/raw/companies.xlsx", skiprows=1)
profitandloss = pd.read_excel("data/raw/profitandloss.xlsx", skiprows=1)
balancesheet = pd.read_excel("data/raw/balancesheet.xlsx", skiprows=1)
cashflow = pd.read_excel("data/raw/cashflow.xlsx", skiprows=1)

# DQ-01 Primary Key Check
print("\nDQ-01 Primary Key Check")
print("Duplicate Company IDs:", companies["id"].duplicated().sum())

# DQ-02 Foreign Key Check
print("\nDQ-02 Foreign Key Check")
invalid_fk = profitandloss[
    ~profitandloss["company_id"].isin(companies["id"])
]
print("Invalid FK Records:", len(invalid_fk))

# DQ-03 Year Validation
print("\nDQ-03 Year Validation")
year_col = pd.to_numeric(profitandloss["year"], errors="coerce")
invalid_years = year_col[
    (year_col.notna()) &
    ((year_col < 2000) | (year_col > 2030))
]
print("Invalid Years:", len(invalid_years))

# DQ-04 Positive Sales
print("\nDQ-04 Positive Sales")
print("Invalid Sales:", len(profitandloss[profitandloss["sales"] <= 0]))

# DQ-05 Positive Assets
print("\nDQ-05 Positive Assets")
print(
    "Invalid Assets:",
    len(balancesheet[balancesheet["total_assets"] <= 0])
)

# DQ-06 Positive Liabilities
print("\nDQ-06 Positive Liabilities")
print(
    "Invalid Liabilities:",
    len(balancesheet[balancesheet["total_liabilities"] <= 0])
)

# DQ-07 Tax Percentage Range
print("\nDQ-07 Tax Percentage Range")
invalid_tax = profitandloss[
    (profitandloss["tax_percentage"] < 0) |
    (profitandloss["tax_percentage"] > 100)
]
print("Invalid Tax %:", len(invalid_tax))

# DQ-08 EPS Null Check
print("\nDQ-08 EPS Null Check")
print("Missing EPS:", profitandloss["eps"].isnull().sum())

# DQ-09 Dividend Payout Check
print("\nDQ-09 Dividend Payout Check")
invalid_dividend = profitandloss[
    profitandloss["dividend_payout"] < 0
]
print("Invalid Dividend Records:", len(invalid_dividend))

# DQ-10 Book Value Check
print("\nDQ-10 Book Value Check")
invalid_book = companies[
    companies["book_value"] <= 0
]
print("Invalid Book Values:", len(invalid_book))

# DQ-11 Face Value Check
print("\nDQ-11 Face Value Check")
invalid_face = companies[
    companies["face_value"] <= 0
]
print("Invalid Face Values:", len(invalid_face))

# DQ-12 ROE Check
print("\nDQ-12 ROE Check")
invalid_roe = companies[
    (companies["roe_percentage"] < -100) |
    (companies["roe_percentage"] > 100)
]
print("Invalid ROE:", len(invalid_roe))

# DQ-13 ROCE Check
print("\nDQ-13 ROCE Check")
invalid_roce = companies[
    (companies["roce_percentage"] < -100) |
    (companies["roce_percentage"] > 100)
]
print("Invalid ROCE:", len(invalid_roce))

# DQ-14 Website Validation
print("\nDQ-14 Website Validation")
print("Missing Websites:", companies["website"].isnull().sum())

# DQ-15 OPM Validation
print("\nDQ-15 OPM Validation")
invalid_opm = profitandloss[
    (profitandloss["opm_percentage"] < -100) |
    (profitandloss["opm_percentage"] > 100)
]
print("Invalid OPM %:", len(invalid_opm))

# DQ-16 Net Profit Validation
print("\nDQ-16 Net Profit Validation")
print(
    "Missing Net Profit:",
    profitandloss["net_profit"].isnull().sum()
)

print("\n==============================")
print("ALL DQ CHECKS COMPLETED")
print("==============================")