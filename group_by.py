mean_price_by_region = df.groupby("region")["price_usd"].mean().sort_values()
