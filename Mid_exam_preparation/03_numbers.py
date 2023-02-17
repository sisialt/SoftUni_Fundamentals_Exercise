sequence = [int(x) for x in input().split()]

average_value = sum(sequence) / len(sequence)

greater_than_average = []
top_numbers = []

for i in range(len(sequence)):
    if sequence[i] > average_value:
        greater_than_average.append(sequence[i])

greater_than_average.sort(reverse=True)

if greater_than_average:
    length_top_greater = min(5, len(greater_than_average))

    for i in range(length_top_greater):
        top_numbers.insert(i, greater_than_average[i])

    print(*top_numbers)

else:
    print("No")


