"""
Sprint 2 - Financial Ratio Engine
Day 8 + Day 9
"""


def calculate_net_profit_margin(net_profit, sales):
    """
    Net Profit Margin = (Net Profit / Sales) * 100
    """
    if sales is None or sales == 0:
        return None

    return round((net_profit / sales) * 100, 2)


def calculate_operating_profit_margin(operating_profit, sales):
    """
    Operating Profit Margin = (Operating Profit / Sales) * 100
    """
    if sales is None or sales == 0:
        return None

    return round((operating_profit / sales) * 100, 2)


def calculate_roe(net_profit, equity_capital, reserves):
    """
    Return on Equity (ROE)
    """

    equity = equity_capital + reserves

    if equity <= 0:
        return None

    return round((net_profit / equity) * 100, 2)


def calculate_roce(
    operating_profit,
    equity_capital,
    reserves,
    borrowings,
):
    """
    Return on Capital Employed
    """

    capital_employed = (
        equity_capital +
        reserves +
        borrowings
    )

    if capital_employed <= 0:
        return None

    return round(
        (operating_profit / capital_employed) * 100,
        2,
    )


def calculate_roa(net_profit, total_assets):
    """
    Return on Assets
    """

    if total_assets <= 0:
        return None

    return round(
        (net_profit / total_assets) * 100,
        2,
    )


# ===================================================
# DAY 9 FUNCTIONS
# ===================================================

def calculate_debt_to_equity(
    borrowings,
    equity_capital,
    reserves,
):
    """
    Debt to Equity Ratio
    """

    equity = equity_capital + reserves

    if borrowings == 0:
        return 0

    if equity <= 0:
        return None

    return round(
        borrowings / equity,
        2,
    )


def calculate_interest_coverage(
    operating_profit,
    interest,
):
    """
    Interest Coverage Ratio
    """

    if interest == 0:
        return None

    return round(
        operating_profit / interest,
        2,
    )


def calculate_net_debt(
    borrowings,
    investments,
):
    """
    Net Debt
    """

    return borrowings - investments


def calculate_asset_turnover(
    sales,
    total_assets,
):
    """
    Asset Turnover Ratio
    """

    if total_assets <= 0:
        return None

    return round(
        sales / total_assets,
        2,
    )


def high_leverage_flag(
    debt_to_equity,
):
    """
    High Leverage Flag
    """

    if debt_to_equity is None:
        return False

    return debt_to_equity > 5


def debt_free_label(
    borrowings,
):
    """
    Debt Free Label
    """

    if borrowings == 0:
        return "Debt Free"

    return "Has Debt"


def icr_warning_flag(
    icr,
):
    """
    Interest Coverage Warning
    """

    if icr is None:
        return False

    return icr < 1.5


# ===================================================
# MAIN
# ===================================================

if __name__ == "__main__":

    print("Net Profit Margin:",
          calculate_net_profit_margin(500, 5000))

    print("Operating Profit Margin:",
          calculate_operating_profit_margin(900, 5000))

    print("ROE:",
          calculate_roe(1000, 2500, 1500))

    print("ROCE:",
          calculate_roce(900, 2500, 1500, 1000))

    print("ROA:",
          calculate_roa(1000, 8000))

    print()

    print("Debt to Equity:",
          calculate_debt_to_equity(500, 300, 200))

    print("Interest Coverage:",
          calculate_interest_coverage(1000, 100))

    print("Net Debt:",
          calculate_net_debt(1000, 300))

    print("Asset Turnover:",
          calculate_asset_turnover(5000, 10000))

    print("High Leverage:",
          high_leverage_flag(6.2))

    print("Debt Free:",
          debt_free_label(0))

    print("ICR Warning:",
          icr_warning_flag(1.2))