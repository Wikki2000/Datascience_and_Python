#!/usr/bin/python3
""" Create a histogram of home sizes. """
import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv("homes.csv")

# Plot the histogram
plt.hist(df["area_m2"], bins=8, color='skyblue', edgecolor='black')
#plt.hist(df["area_m2"])

# Set axis labels and title
plt.xlabel("Area [sq meters]")
plt.ylabel("Frequency")
plt.title("Distribution of Home Sizes")

# Show the plot
plt.tight_layout()
#plt.show()
plt.savefig("home_sizes_histogram.png")  # Save plot as PNG file
