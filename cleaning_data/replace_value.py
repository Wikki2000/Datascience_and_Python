#!/usr/bin/python3
""" Replace all missing data with a given value. """
from functions import dataframe, replace_all_by

df = dataframe()
print(replace_all_by("New Value", df).head())
