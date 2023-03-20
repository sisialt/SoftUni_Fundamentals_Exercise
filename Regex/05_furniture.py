import re

line = input()

bought_items = []
total_price = 0

while line != "Purchase":
    pattern = r"^>>(?P<furniture>[A-Za-z]+)<<(?P<price>\d+\.?\d+)!(?P<quantity>\d+$)"

    # matches = re.findall(pattern, line)
    # if not matches:
    #     line = input()
    #     continue
    #
    # match = matches[0]
    #
    # item = match[0]
    # price = float(match[1])
    # quantity = int(match[2])
    #
    # bought_items.append(item)
    # total_price += price * quantity
    #
    # line = input()

    match = re.match(pattern, line)
    if not match:
        line = input()
        continue

    groups = match.groupdict()

    bought_items.append(groups["furniture"])
    total_price += float(groups["price"]) * int(groups["quantity"])

    line = input()

print("Bought furniture:")
for item in bought_items:
    print(item)
print(f"Total money spend: {total_price:.2f}")
