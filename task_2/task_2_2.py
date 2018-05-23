dollars = int(input("Input dollars: "))
cents = int(input("Input cents: "))
count = int(input("Input items count: "))
total_price = float(dollars + cents / 100) * count
print("Total: %d dollars %d cents" % (total_price, (total_price * 100) % 100))
