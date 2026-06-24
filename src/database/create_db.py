import sqlite3

conn = sqlite3.connect("nifty100.db")
cursor = conn.cursor()

# Companies
cursor.execute("""
CREATE TABLE companies (
    id TEXT PRIMARY KEY,
    company_logo TEXT,
    company_name TEXT,
    chart_link TEXT,
    about_company TEXT,
    website TEXT,
    nse_profile TEXT,
    bse_profile TEXT,
    face_value REAL,
    book_value REAL,
    roce_percentage REAL,
    roe_percentage REAL
)
""")

# Profit & Loss
cursor.execute("""
CREATE TABLE profitandloss (
    id INTEGER PRIMARY KEY,
    company_id TEXT,
    year TEXT,
    sales REAL,
    expenses REAL,
    operating_profit REAL,
    opm_percentage REAL,
    other_income REAL,
    interest REAL,
    depreciation REAL,
    profit_before_tax REAL,
    tax_percentage REAL,
    net_profit REAL,
    eps REAL,
    dividend_payout REAL
)
""")

# Balance Sheet
cursor.execute("""
CREATE TABLE balancesheet (
    id INTEGER PRIMARY KEY,
    company_id TEXT,
    year TEXT,
    equity_capital REAL,
    reserves REAL,
    borrowings REAL,
    other_liabilities REAL,
    total_liabilities REAL,
    fixed_assets REAL,
    cwip REAL,
    investments REAL,
    other_asset REAL,
    total_assets REAL
)
""")

# Cash Flow
cursor.execute("""
CREATE TABLE cashflow (
    id INTEGER PRIMARY KEY,
    company_id TEXT,
    year TEXT,
    operating_activity REAL,
    investing_activity REAL,
    financing_activity REAL,
    net_cash_flow REAL
)
""")

# Analysis
cursor.execute("""
CREATE TABLE analysis (
    id INTEGER PRIMARY KEY,
    company_id TEXT,
    compounded_sales_growth REAL,
    compounded_profit_growth REAL,
    stock_price_cagr REAL,
    roe REAL
)
""")

# Documents
cursor.execute("""
CREATE TABLE documents (
    id INTEGER PRIMARY KEY,
    company_id TEXT,
    year TEXT,
    annual_report TEXT
)
""")

# Pros & Cons
cursor.execute("""
CREATE TABLE prosandcons (
    id INTEGER PRIMARY KEY,
    company_id TEXT,
    pros TEXT,
    cons TEXT
)
""")

# Sectors
cursor.execute("""
CREATE TABLE sectors (
    id INTEGER PRIMARY KEY,
    company_id TEXT,
    broad_sector TEXT,
    sub_sector TEXT,
    index_weight_pct REAL,
    market_cap_category TEXT
)
""")

# Stock Prices
cursor.execute("""
CREATE TABLE stock_prices (
    id INTEGER PRIMARY KEY,
    company_id TEXT,
    date TEXT,
    open_price REAL,
    high_price REAL,
    low_price REAL,
    close_price REAL,
    volume INTEGER,
    adjusted_close REAL
)
""")

# Financial Ratios
cursor.execute("""
CREATE TABLE financial_ratios (
    id INTEGER PRIMARY KEY,
    company_id TEXT,
    year TEXT,
    net_profit_margin_pct REAL,
    operating_profit_margin_pct REAL,
    return_on_equity_pct REAL,
    debt_to_equity REAL,
    interest_coverage REAL,
    asset_turnover REAL,
    free_cash_flow_cr REAL,
    capex_cr REAL,
    earnings_per_share REAL,
    book_value_per_share REAL,
    dividend_payout_ratio_pct REAL,
    total_debt_cr REAL,
    cash_from_operations_cr REAL
)
""")

# Peer Groups
cursor.execute("""
CREATE TABLE peer_groups (
    id INTEGER PRIMARY KEY,
    peer_group_name TEXT,
    company_id TEXT,
    is_benchmark TEXT
)
""")

conn.commit()
conn.close()

print("Database created successfully!")