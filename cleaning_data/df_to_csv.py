import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 22],
    "Grade": ["A", "B", "A"]
}

df = pd.DataFrame(data)

# Save it to a CSV file
df.to_csv("students.csv", index=False)

