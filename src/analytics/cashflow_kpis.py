"""
Sprint 2 - Day 11
Cash Flow KPI Engine
"""


def calculate_free_cash_flow(operating_activity, investing_activity):
    """
    Free Cash Flow = Operating Activity + Investing Activity
    """
    return operating_activity + investing_activity


def calculate_cfo_quality_ratio(operating_activity, net_profit):
    """
    CFO Quality Ratio = CFO / Net Profit
    """

    if net_profit == 0:
        return None

    return round(operating_activity / net_profit, 2)


def calculate_capex_intensity(investing_activity, sales):
    """
    CapEx Intensity = |Investing Activity| / Sales × 100
    """

    if sales == 0:
        return None

    return round(abs(investing_activity) / sales * 100, 2)


def calculate_fcf_conversion(free_cash_flow, operating_profit):
    """
    FCF Conversion = FCF / Operating Profit × 100
    """

    if operating_profit == 0:
        return None

    return round(free_cash_flow / operating_profit * 100, 2)


def classify_capital_allocation(cfo, cfi, cff):
    """
    Capital Allocation Pattern
    """

    pattern = (
        "+" if cfo >= 0 else "-",
        "+" if cfi >= 0 else "-",
        "+" if cff >= 0 else "-"
    )

    mapping = {
        ("+", "-", "-"): "Reinvestor",
        ("+", "-", "+"): "Shareholder Returns",
        ("+", "+", "-"): "Liquidating Assets",
        ("-", "+", "+"): "Distress Signal",
        ("-", "-", "+"): "Growth Funded by Debt",
        ("+", "+", "+"): "Cash Accumulator",
        ("-", "-", "-"): "Pre-Revenue",
    }

    return mapping.get(pattern, "Mixed")


if __name__ == "__main__":

    fcf = calculate_free_cash_flow(1000, -300)

    print("Free Cash Flow:", fcf)

    print(
        "CFO Quality:",
        calculate_cfo_quality_ratio(1000, 800)
    )

    print(
        "CapEx Intensity:",
        calculate_capex_intensity(-300, 5000)
    )

    print(
        "FCF Conversion:",
        calculate_fcf_conversion(fcf, 900)
    )

    print(
        "Capital Allocation:",
        classify_capital_allocation(
            1000,
            -300,
            -200
        )
    )