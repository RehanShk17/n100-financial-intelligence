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
    calculate_net_profit_margin,
    calculate_operating_profit_margin,
    calculate_roe,
    calculate_roce,
    calculate_roa,
)

# -----------------------------
# Test 1 - Net Profit Margin
# -----------------------------

def test_net_profit_margin():
    assert calculate_net_profit_margin(100, 1000) == 10.0


# -----------------------------
# Test 2 - Net Profit Margin
# Zero Sales
# -----------------------------

def test_net_profit_margin_zero_sales():
    assert calculate_net_profit_margin(100, 0) is None


# -----------------------------
# Test 3 - Operating Profit Margin
# -----------------------------

def test_operating_profit_margin():
    assert calculate_operating_profit_margin(200, 1000) == 20.0


# -----------------------------
# Test 4 - OPM Zero Sales
# -----------------------------

def test_operating_profit_margin_zero_sales():
    assert calculate_operating_profit_margin(200, 0) is None


# -----------------------------
# Test 5 - ROE
# -----------------------------

def test_roe():
    assert calculate_roe(100, 300, 200) == 20.0


# -----------------------------
# Test 6 - ROE Negative Equity
# -----------------------------

def test_roe_negative_equity():
    assert calculate_roe(100, -200, 100) is None


# -----------------------------
# Test 7 - ROCE
# -----------------------------

def test_roce():
    assert calculate_roce(150, 500, 300, 200) == 15.0


# -----------------------------
# Test 8 - ROA
# -----------------------------

def test_roa():
    assert calculate_roa(100, 1000) == 10.0