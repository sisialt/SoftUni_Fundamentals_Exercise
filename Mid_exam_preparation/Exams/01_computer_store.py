total_price = 0

while True:
    price = input()

    if price != "special" and price != "regular":
        price = float(price)
        if price <= 0:
            print("Invalid price!")
            continue

        total_price += price
    else:
        break

total_price_with_taxes = total_price * 1.2
taxes = total_price * 0.2

if price == "special":
    total_price_with_taxes *= 0.9

if total_price == 0:
    print("Invalid order!")
else:
    print(f"Congratulations you've just bought a new computer!\nPrice without taxes: {total_price:.2f}$\nTaxes: \
{taxes:.2f}$\n-----------\nTotal price: {total_price_with_taxes:.2f}$")
