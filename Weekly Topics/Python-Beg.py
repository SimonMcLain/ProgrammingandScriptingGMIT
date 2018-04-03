cost = 14.99
taxperc = 23

tax = taxperc / 100.00

salepr = cost * (1.0 + tax)

print("sale price:", salepr)