import pandas as pd

companies = pd.read_excel("data/raw/companies.xlsx", skiprows=1)
profitandloss = pd.read_excel("data/raw/profitandloss.xlsx", skiprows=1)
balancesheet = pd.read_excel("data/raw/balancesheet.xlsx", skiprows=1)
cashflow = pd.read_excel("data/raw/cashflow.xlsx", skiprows=1)

# ---------- COMPANIES TESTS ----------

def test_companies_loaded():
    assert len(companies) > 0

def test_companies_has_id():
    assert "id" in companies.columns

def test_companies_has_name():
    assert "company_name" in companies.columns

def test_companies_pk_unique():
    assert companies["id"].duplicated().sum() == 0

def test_company_name_not_null():
    assert companies["company_name"].isnull().sum() == 0

def test_book_value_exists():
    assert "book_value" in companies.columns

def test_face_value_exists():
    assert "face_value" in companies.columns

def test_website_exists():
    assert "website" in companies.columns

# ---------- PROFIT & LOSS TESTS ----------

def test_profitandloss_loaded():
    assert len(profitandloss) > 0

def test_sales_exists():
    assert "sales" in profitandloss.columns

def test_expenses_exists():
    assert "expenses" in profitandloss.columns

def test_net_profit_exists():
    assert "net_profit" in profitandloss.columns

def test_company_id_exists():
    assert "company_id" in profitandloss.columns

def test_year_exists():
    assert "year" in profitandloss.columns

def test_eps_exists():
    assert "eps" in profitandloss.columns

def test_tax_percentage_exists():
    assert "tax_percentage" in profitandloss.columns

# ---------- BALANCE SHEET TESTS ----------

def test_balancesheet_loaded():
    assert len(balancesheet) > 0

def test_total_assets_exists():
    assert "total_assets" in balancesheet.columns

def test_total_liabilities_exists():
    assert "total_liabilities" in balancesheet.columns

def test_reserves_exists():
    assert "reserves" in balancesheet.columns

def test_borrowings_exists():
    assert "borrowings" in balancesheet.columns

def test_equity_capital_exists():
    assert "equity_capital" in balancesheet.columns

# ---------- CASHFLOW TESTS ----------

def test_cashflow_loaded():
    assert len(cashflow) > 0

def test_operating_activity_exists():
    assert "operating_activity" in cashflow.columns

def test_investing_activity_exists():
    assert "investing_activity" in cashflow.columns

def test_financing_activity_exists():
    assert "financing_activity" in cashflow.columns

def test_net_cash_flow_exists():
    assert "net_cash_flow" in cashflow.columns

# ---------- DATA QUALITY TESTS ----------

def test_company_pk_unique():
    assert companies["id"].duplicated().sum() == 0

def test_profitloss_pk_unique():
    assert profitandloss["id"].duplicated().sum() == 0

def test_balancesheet_pk_unique():
    assert balancesheet["id"].duplicated().sum() == 0

def test_cashflow_pk_unique():
    assert cashflow["id"].duplicated().sum() == 0

def test_year_column_exists():
    assert "year" in profitandloss.columns

def test_year_not_null():
    assert profitandloss["year"].isnull().sum() < len(profitandloss)

def test_company_count():
    assert len(companies) == 92

def test_profitloss_count():
    assert len(profitandloss) == 1276

def test_balancesheet_count():
    assert len(balancesheet) == 1312

def test_cashflow_count():
    assert len(cashflow) == 1187