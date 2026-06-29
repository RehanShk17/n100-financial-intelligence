"""
Sprint 2 - Day 8
Financial Ratio Engine
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
    ROE = Net Profit / (Equity Capital + Reserves) * 100
    """

    equity = equity_capital + reserves

    if equity <= 0:
        return None

    return round((net_profit / equity) * 100, 2)


def calculate_roce(operating_profit,
                   equity_capital,
                   reserves,
                   borrowings):
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
        2
    )


def calculate_roa(net_profit, total_assets):
    """
    Return on Assets
    """

    if total_assets <= 0:
        return None

    return round(
        (net_profit / total_assets) * 100,
        2
    )


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