#!/usr/bin/python3
""" Display column and number of empty rows. """
from functions import dataframe, missing_data

df = dataframe()
print(missing_data(df))
