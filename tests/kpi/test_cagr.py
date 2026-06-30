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

from cagr import calculate_cagr


# ------------------------------------------------
# Test 1 - Normal CAGR
# ------------------------------------------------

def test_normal_cagr():

    value, flag = calculate_cagr(100, 200, 5)

    assert round(value, 2) == 14.87
    assert flag == "SUCCESS"


# ------------------------------------------------
# Test 2 - Zero Base
# ------------------------------------------------

def test_zero_base():

    value, flag = calculate_cagr(0, 200, 5)

    assert value is None
    assert flag == "ZERO_BASE"


# ------------------------------------------------
# Test 3 - Turnaround
# ------------------------------------------------

def test_turnaround():

    value, flag = calculate_cagr(-100, 200, 5)

    assert value is None
    assert flag == "TURNAROUND"


# ------------------------------------------------
# Test 4 - Decline To Loss
# ------------------------------------------------

def test_decline_to_loss():

    value, flag = calculate_cagr(100, -50, 5)

    assert value is None
    assert flag == "DECLINE_TO_LOSS"


# ------------------------------------------------
# Test 5 - Both Negative
# ------------------------------------------------

def test_both_negative():

    value, flag = calculate_cagr(-100, -50, 5)

    assert value is None
    assert flag == "BOTH_NEGATIVE"


# ------------------------------------------------
# Test 6 - Invalid Years
# ------------------------------------------------

def test_invalid_years():

    value, flag = calculate_cagr(100, 200, 0)

    assert value is None
    assert flag == "INVALID_YEARS"


# ------------------------------------------------
# Test 7 - Positive Growth
# ------------------------------------------------

def test_positive_growth():

    value, flag = calculate_cagr(500, 1000, 10)

    assert value > 0
    assert flag == "SUCCESS"


# ------------------------------------------------
# Test 8 - Negative Growth
# ------------------------------------------------

def test_negative_growth():

    value, flag = calculate_cagr(1000, 500, 5)

    assert value < 0
    assert flag == "SUCCESS"


# ------------------------------------------------
# Test 9 - Return Type
# ------------------------------------------------

def test_return_type():

    value, flag = calculate_cagr(100, 200, 5)

    assert isinstance(flag, str)


# ------------------------------------------------
# Test 10 - Float Output
# ------------------------------------------------

def test_float_output():

    value, flag = calculate_cagr(100, 200, 5)

    assert isinstance(value, float)