#!/usr/bin/python3

import pandas as pd


def dataframe():
    """ Read CSV into data frame. """
    df = pd.read_csv("data.csv")
    return df


def missing_data(df):
    """ Count rows with missing value. """
    return df.isnull().sum()


def replace_all_by(value_to_replace, df):
    """Replace all rows with missing data with given value.
    """
    return df.fillna(value_to_replace)


def drop_missing_row(df):
    """ Drop all rows with missing data. """
    # df.dropna(inplace=True)  # If only you want to modify the data.
    return df.dropna()


def remove_duplicate(df):
    """ Remove all duplicated data. """
    # df.drop_duplicates(inplace=True)
    return df.drop_duplicates()

"""
df.columns = df.columns.str.strip()        # Remove whitespace
df.columns = df.columns.str.lower()        # Convert to lowercase
df.rename(columns={"student name": "name"}, inplace=True)  # Rename
df['age'] = df['age'].astype(int)
df = df[df['age'] > 0]  # Remove rows with invalid age
df1.drop(columns=["state"], inplace=True)  # Drop a column call state.
"""
