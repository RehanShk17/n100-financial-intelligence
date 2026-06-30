"""
Sprint 2 - Day 10
CAGR Engine
"""


def calculate_cagr(start_value, end_value, years):
    """
    Calculate CAGR
    CAGR = ((End / Start) ** (1 / Years) - 1) * 100
    """

    if years <= 0:
        return None, "INVALID_YEARS"

    if start_value == 0:
        return None, "ZERO_BASE"

    if start_value < 0 and end_value < 0:
        return None, "BOTH_NEGATIVE"

    if start_value < 0 and end_value > 0:
        return None, "TURNAROUND"

    if start_value > 0 and end_value < 0:
        return None, "DECLINE_TO_LOSS"

    cagr = (
        ((end_value / start_value) ** (1 / years)) - 1
    ) * 100

    return round(cagr, 2), "SUCCESS"


if __name__ == "__main__":

    print("Normal Growth:",
          calculate_cagr(100, 200, 5))

    print("Zero Base:",
          calculate_cagr(0, 200, 5))

    print("Turnaround:",
          calculate_cagr(-100, 200, 5))

    print("Decline:",
          calculate_cagr(100, -50, 5))

    print("Both Negative:",
          calculate_cagr(-100, -50, 5))