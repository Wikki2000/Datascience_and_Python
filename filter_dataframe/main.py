#!/usr/bin/python3
"""Create a subset using mask."""
import pandas as pd


df = pd.read_csv("data.csv")
print("Total Row: ", len(df))

# Create subset for property in `"Federal Capital"`.
mask_ba = df["place_with_parent_names"].str.contains("Capital Federal")

# Create Subset for apartment property
mask_apt = df["property_type"] == "apartment"

# Create Subset for price lesser than 
mask_price = df["price_aprox_usd"] < 40_000

df = df[mask_ba & mask_ba & mask_price]
print("Subset Row Count", len(df))
