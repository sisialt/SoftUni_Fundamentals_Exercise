input_data = input()

products = {}

while input_data != "buy":
    name, price, quantity = input_data.split()

    if name not in products:
        products[name] = [float(price), int(quantity)]
    else:
        products[name][1] += int(quantity)
        products[name][0] = float(price)

    input_data = input()

for key, value in products.items():
    print(f"{key} -> {value[0] * value[1]:.2f}")
    