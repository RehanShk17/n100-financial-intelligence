-- Total Companies
SELECT COUNT(*) FROM companies;

-- Top 10 Companies by Book Value
SELECT company_name, book_value
FROM companies
ORDER BY book_value DESC
LIMIT 10;

-- Profit & Loss Records
SELECT COUNT(*) FROM profitandloss;

-- Balance Sheet Records
SELECT COUNT(*) FROM balancesheet;

-- Cash Flow Records
SELECT COUNT(*) FROM cashflow;

-- Companies with Highest ROE
SELECT company_name, roe_percentage
FROM companies
ORDER BY roe_percentage DESC
LIMIT 10;

-- Companies with Highest ROCE
SELECT company_name, roce_percentage
FROM companies
ORDER BY roce_percentage DESC
LIMIT 10;

-- Average Book Value
SELECT AVG(book_value)
FROM companies;

-- Year Coverage
SELECT MIN(year), MAX(year)
FROM profitandloss;

-- Sample Financial Records
SELECT *
FROM profitandloss
LIMIT 10;