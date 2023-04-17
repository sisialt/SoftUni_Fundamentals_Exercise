numbers = [float(x) for x in input().split()]

absolute_numbers = []

for num in numbers:
    absolute_numbers.append(abs(num))

print(absolute_numbers)