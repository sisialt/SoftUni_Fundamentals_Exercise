input_data = input().split()

products = {}

for i in range(0, len(input_data), 2):
    products[input_data[i]] = int(input_data[i + 1])

print(products)
