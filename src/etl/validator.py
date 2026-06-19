import pandas as pd

# Store all validation failures
failures = []


def check_missing_values(df, table_name):
    missing = df.isnull().sum()

    print(f"\n=== {table_name} Missing Values ===")

    for col, count in missing.items():
        if count > 0:
            print(f"{col}: {count}")

            failures.append({
                "table": table_name,
                "rule": "Missing Values",
                "column": col,
                "count": int(count)
            })


def check_duplicates(df, table_name):
    duplicates = df.duplicated().sum()

    print(f"\n=== {table_name} Duplicates ===")
    print(f"Duplicate Rows: {duplicates}")

    if duplicates > 0:
        failures.append({
            "table": table_name,
            "rule": "Duplicate Rows",
            "column": "ALL",
            "count": int(duplicates)
        })


def check_primary_key(df, column, table_name):
    duplicates = df[column].duplicated().sum()

    print(f"\n=== PK Check: {table_name}.{column} ===")
    print(f"Duplicate Keys: {duplicates}")

    if duplicates > 0:
        failures.append({
            "table": table_name,
            "rule": "Duplicate Primary Key",
            "column": column,
            "count": int(duplicates)
        })


def check_year(df, table_name):

    if "year" not in df.columns:
        return

    year_col = pd.to_numeric(df["year"], errors="coerce")

    invalid_years = year_col[
        (year_col.notna()) &
        (
            (year_col < 2000) |
            (year_col > 2030)
        )
    ]

    print(f"\n=== Year Validation: {table_name} ===")
    print(f"Invalid Years: {len(invalid_years)}")

    if len(invalid_years) > 0:
        failures.append({
            "table": table_name,
            "rule": "Invalid Year",
            "column": "year",
            "count": int(len(invalid_years))
        })


if __name__ == "__main__":

    files = {
        "companies": "data/raw/companies.xlsx",
        "profitandloss": "data/raw/profitandloss.xlsx",
        "balancesheet": "data/raw/balancesheet.xlsx",
        "cashflow": "data/raw/cashflow.xlsx"
    }

    for name, path in files.items():

        df = pd.read_excel(path, skiprows=1)

        check_missing_values(df, name)

        check_duplicates(df, name)

        if "id" in df.columns:
            check_primary_key(df, "id", name)

        if "year" in df.columns:
            check_year(df, name)

    # Generate CSV report
    if failures:

        report = pd.DataFrame(failures)

        report.to_csv(
            "output/validation_failures.csv",
            index=False
        )

        print("\nvalidation_failures.csv generated successfully")

    else:
        print("\nNo validation failures found.")