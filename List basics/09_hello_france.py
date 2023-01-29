items = input().split("|")
budget = float(input())

new_prices = []
rest_budget = budget
profit = 0

for item in items:
    item_args = item.split("->")
    item_type = item_args[0]
    item_price = float(item_args[1])

    if item_type == "Clothes":
        if item_price <= 50 and rest_budget >= item_price:
            rest_budget -= item_price
            new_price = "{:.2f}".format(item_price * 1.4)
            new_prices.append(new_price)
            profit += item_price * 0.4

    elif item_type == "Shoes":
        if item_price <= 35 and rest_budget >= item_price:
            rest_budget -= item_price
            new_price = "{:.2f}".format(item_price * 1.4)
            new_prices.append(new_price)
            profit += item_price * 0.4

    elif item_type == "Accessories":
        if item_price <= 20.5 and rest_budget >= item_price:
            rest_budget -= item_price
            new_price = "{:.2f}".format(item_price * 1.4)
            new_prices.append(new_price)
            profit += item_price * 0.4

print(" ".join(new_prices))
print(f"Profit: {profit:.2f}")

if budget + profit >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")

