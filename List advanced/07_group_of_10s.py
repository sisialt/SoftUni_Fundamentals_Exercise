numbers = [int(x) for x in input().split(", ")]

numbers_filtered = numbers.copy()

bottom_limit, upper_limit = 0, 10

while numbers_filtered:
    group = []

    for num in numbers:
        if bottom_limit < num <= upper_limit:
            group.append(num)
            numbers_filtered.remove(num)

    print(f"Group of {upper_limit}'s: {group}")

    bottom_limit += 10
    upper_limit += 10
    numbers = numbers_filtered.copy()

