#!/usr/bin/python3
""" Get some column from Data Frame. """
import pandas as pd


df = pd.read_csv("students.csv")
print(df.columns)  # Get list of all columns
new_df = df[["Department", "Fee"]]
print(new_df)
