import pandas as pd

df1 = pd.DataFrame({
    "Name": ["Alice", "Bob"],
    "Age": [25, 30]
})

df2 = pd.DataFrame({
    "Name": ["Charlie", "David"],
    "Age": [22, 28]
})

# Concatenate vertically (default)
result = pd.concat([df1, df2], ignore_index=True)

print(result)

"""
result = pd.concat([df1, df2], axis=1)  #  Horizontal concat (side by side)
result = pd.concat([df1, df2], ignore_index=True)  # Ignore old index and reset to default
result = pd.concat([df1, df2], keys=["Group A", "Group B"])  # Add column for source
"""
