#!/usr/bin/python3
""" Create a Data Frame. """
import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Paris', 'London']
}

# By default the key becomes the column
df = pd.DataFrame.from_dict(data)
print(df)

# Set key as index
print("Setting Key as Index")
df = pd.DataFrame.from_dict(data, orient="index")
print(df)

# Set Column
df = pd.DataFrame.from_dict(data, orient="index", columns=["A", "B", "C"])
print(df)
