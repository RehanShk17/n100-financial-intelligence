import pandas as pd

def check_positive(df, column):
    return df[df[column] <= 0]

def check_null(df, column):
    return df[df[column].isnull()]

def check_duplicates(df, column):
    return df[df[column].duplicated()]

def check_range(df, column, min_val, max_val):
    return df[(df[column] < min_val) | (df[column] > max_val)]