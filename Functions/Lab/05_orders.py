def calculate_price(order, n):
    total_price = 0
    if order == "coffee":
        total_price = n * 1.50
    elif order == "water":
        total_price = n * 1
    elif order == "coke":
        total_price = n * 1.40
    elif order == "snacks":
        total_price = n * 2
    return total_price


product = input()
quantity = int(input())

print(f"{calculate_price(product, quantity):.2f}")