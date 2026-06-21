stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150
}

total_investment = 0

while True:
    stock = input("Enter stock name (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock in stock_prices:
        quantity = int(input("Enter quantity: "))
        total_investment += stock_prices[stock] * quantity
    else:
        print("Stock not found.")

print("Total Investment Value: $", total_investment)
