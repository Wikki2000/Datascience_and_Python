import pandas as pd

df = pd.read_csv("students.csv")
print("********* 5 Rows ***********")
print(df.head()) # print 5 row by default

print("********* 7 Rows ***********")
print(df.head(7))  # Prinit 10 row

print("********* All Rows ***********")
print(df["Department"])  # Print a particular column
