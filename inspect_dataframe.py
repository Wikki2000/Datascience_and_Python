#!/usr/bin/python3
""" Inspect a Data Frame. """
import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Paris', 'London']
}

df = pd.DataFrame.from_dict(data)
print(df.shape)
print(df.info())
