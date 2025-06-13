cleaned_price = df1["price_usd"].replace(r"[$, ]", "", regex=True).astype(float)
df1["price_usd"] = cleaned_price
