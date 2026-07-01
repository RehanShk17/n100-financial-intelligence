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

from cashflow_kpis import (
    calculate_free_cash_flow,
    calculate_cfo_quality_ratio,
    calculate_capex_intensity,
    calculate_fcf_conversion,
    classify_capital_allocation
)


# ----------------------------------------
# Test 1 - Free Cash Flow
# ----------------------------------------

def test_free_cash_flow():

    assert calculate_free_cash_flow(1000, -300) == 700


# ----------------------------------------
# Test 2 - CFO Quality Ratio
# ----------------------------------------

def test_cfo_quality_ratio():

    assert calculate_cfo_quality_ratio(1000, 800) == 1.25


# ----------------------------------------
# Test 3 - CFO Quality Zero Profit
# ----------------------------------------

def test_cfo_quality_zero_profit():

    assert calculate_cfo_quality_ratio(1000, 0) is None


# ----------------------------------------
# Test 4 - CapEx Intensity
# ----------------------------------------

def test_capex_intensity():

    assert calculate_capex_intensity(-300, 5000) == 6.0


# ----------------------------------------
# Test 5 - CapEx Zero Sales
# ----------------------------------------

def test_capex_zero_sales():

    assert calculate_capex_intensity(-300, 0) is None


# ----------------------------------------
# Test 6 - FCF Conversion
# ----------------------------------------

def test_fcf_conversion():

    fcf = calculate_free_cash_flow(1000, -300)

    assert calculate_fcf_conversion(fcf, 900) == 77.78


# ----------------------------------------
# Test 7 - FCF Conversion Zero OP
# ----------------------------------------

def test_fcf_conversion_zero_op():

    assert calculate_fcf_conversion(700, 0) is None


# ----------------------------------------
# Test 8 - Capital Allocation Patterns
# ----------------------------------------

def test_capital_allocation_patterns():

    assert classify_capital_allocation(
        1000,
        -300,
        -200
    ) == "Reinvestor"

    assert classify_capital_allocation(
        1000,
        -300,
        400
    ) == "Shareholder Returns"

    assert classify_capital_allocation(
        -100,
        -200,
        300
    ) == "Growth Funded by Debt"

    assert classify_capital_allocation(
        500,
        300,
        200
    ) == "Cash Accumulator"