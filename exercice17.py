price_base = {"Laser sword": 229.0,"Mitendo DX": 127.30,"Linux cushion": 74.50,"Goldorak briefs": 29.90,"Nextpresso station": 184.60}
print(price_base)
total_price = sum(price_base.values())
print(total_price)
del price_base["Linux cushion"]
print(price_base)