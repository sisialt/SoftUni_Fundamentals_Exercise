import re

n = int(input())

pattern_valid_barcode = r"@#+[A-Z][A-Za-z\d]{4,}[A-Z]@#+"
pattern_digit = r"\d"

for _ in range(n):
    line = input()

    matches = re.findall(pattern_valid_barcode, line)
    if not matches:
        print("Invalid barcode")
    else:
        numbers = re.findall(pattern_digit, matches[0])
        if not numbers:
            product_group = "00"
        else:
            product_group = "".join(numbers)

        print(f"Product group: {product_group}")


