numbers = [int(x) for x in input().split(", ")]

even_numbers_indices = [i for i in range(len(numbers)) if numbers[i] % 2 == 0]
print(even_numbers_indices)
