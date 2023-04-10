input_data = input().split()
searched_products = input().split()

products = {}

for i in range(0, len(input_data), 2):
    products[input_data[i]] = int(input_data[i + 1])

for product in searched_products:
    if product in products:
        print(f"We have {products[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")