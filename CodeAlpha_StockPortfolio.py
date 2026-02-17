stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 320
}

total_investment = 0

print("Available Stocks:", stock_prices)

while True:
    stock = input("Enter stock name (or 'done' to finish): ").upper()
    
    if stock == "DONE":
        break
    
    if stock in stock_prices:
        quantity = int(input("Enter quantity: "))
        total_investment += stock_prices[stock] * quantity
    else:
        print("Stock not available.")

print("Total Investment Value:", total_investment)

with open("portfolio.txt", "w") as file:
    file.write("Total Investment Value: " + str(total_investment))
