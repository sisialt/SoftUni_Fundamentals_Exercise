divisor = int(input())
boundary = int(input())

for largest_number in range(boundary, 0, -1):
    if largest_number % divisor == 0:
        print(largest_number)
        break