import sys
import os

# Add src/analytics to Python path
sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "../../src/analytics"
        )
    )
)

from ratios import (
    calculate_debt_to_equity,
    calculate_interest_coverage,
    calculate_net_debt,
    calculate_asset_turnover,
    high_leverage_flag,
    debt_free_label,
    icr_warning_flag,
)

# ---------------------------------------
# Test 1 - Debt to Equity
# ---------------------------------------

def test_debt_to_equity():
    assert calculate_debt_to_equity(500, 300, 200) == 1.0


# ---------------------------------------
# Test 2 - Debt Free Company
# ---------------------------------------

def test_debt_to_equity_zero_borrowing():
    assert calculate_debt_to_equity(0, 300, 200) == 0


# ---------------------------------------
# Test 3 - Negative Equity
# ---------------------------------------

def test_debt_to_equity_negative_equity():
    assert calculate_debt_to_equity(500, -300, 100) is None


# ---------------------------------------
# Test 4 - Interest Coverage
# ---------------------------------------

def test_interest_coverage():
    assert calculate_interest_coverage(1000, 100) == 10.0


# ---------------------------------------
# Test 5 - Interest = 0
# ---------------------------------------

def test_interest_coverage_zero_interest():
    assert calculate_interest_coverage(1000, 0) is None


# ---------------------------------------
# Test 6 - Net Debt
# ---------------------------------------

def test_net_debt():
    assert calculate_net_debt(1000, 300) == 700


# ---------------------------------------
# Test 7 - Asset Turnover
# ---------------------------------------

def test_asset_turnover():
    assert calculate_asset_turnover(5000, 10000) == 0.5


# ---------------------------------------
# Test 8 - Flags
# ---------------------------------------

def test_flags():

    assert high_leverage_flag(6.5) is True

    assert high_leverage_flag(2.5) is False

    assert debt_free_label(0) == "Debt Free"

    assert debt_free_label(100) == "Has Debt"

    assert icr_warning_flag(1.2) is True

    assert icr_warning_flag(3.0) is False