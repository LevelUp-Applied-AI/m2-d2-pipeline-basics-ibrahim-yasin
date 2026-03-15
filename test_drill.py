"""
Module 2 — Drill 2: Learner Test File

Write your two pytest test functions below.
The autograder will run these as part of the CI check.
"""

import pandas as pd
import numpy as np
from drill_functions import clean_column, compute_revenue


def test_clean_column():
    s = pd.Series([1, 2, np.nan, 4, 5])
    cleaned = clean_column(s)
    assert cleaned.isna().sum() == 0, "No NaN should remain after cleaning"
    expected_median = s.median()  
    assert cleaned[2] == expected_median, f"NaN should be replaced with median {expected_median}"
    pass 


def test_compute_revenue():
    quantity = pd.Series([2, 3, 4])
    price = pd.Series([10, 20, 30])
    
    revenue = compute_revenue(quantity, price)
    
    expected = pd.Series([20, 60, 120])
    pd.testing.assert_series_equal(revenue, expected, check_names=False)
    pass
