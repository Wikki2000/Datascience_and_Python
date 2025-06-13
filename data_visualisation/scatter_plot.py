#!/usr/bin/python3
"""Visualise Scatter Plot and Save to File."""
import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv("homes.csv")

# Create scatter plot
plt.scatter(df["area_m2"], df["price_usd"], marker="x", color="blue", label="Data Point")

# Label each axes and add graph title.
plt.xlabel("Surface Area [Sq Metres]")
plt.ylabel("Price [USD]")
plt.title("Price Trends Relative to Surface Area")

plt.legend()  # Show legend "Data Points"

# Save the figure to file (e.g., PNG)
plt.savefig("price_vs_surface_area.png", dpi=300, bbox_inches='tight')

# Display the plot
#plt.show()
