elements = input()

products = {}

while elements != "statistics":
    elements = elements.split(": ")
    product = elements[0]
    quantity = int(elements[1])

    if product not in products:
        products[product] = quantity
    else:
        products[product] += quantity

    elements = input()

print("Products in stock:")
for product, quantity in products.items():
    print(f"- {product}: {quantity}")
print(f"Total Products: {len(products)}\nTotal Quantity: {sum(products.values())}")
