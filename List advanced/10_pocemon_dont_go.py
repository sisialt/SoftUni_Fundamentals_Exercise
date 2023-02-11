sequence = [int(x) for x in input().split()]
sum_elements = 0

while sequence:
    index = int(input())

    if index < 0:
        el_to_remove = sequence[0]
        sum_elements += el_to_remove
        sequence.pop(0)
        sequence.append(sequence[-1])
    elif index >= len(sequence):
        el_to_remove = sequence[-1]
        sum_elements += el_to_remove
        sequence.pop(-1)
        sequence.append(sequence[0])
    else:
        el_to_remove = sequence[index]
        sum_elements += el_to_remove
        sequence.pop(index)

    for i in range(0, len(sequence)):
        if sequence[i] <= el_to_remove:
            sequence[i] += el_to_remove
        else:
            sequence[i] -= el_to_remove

print(sum_elements)

# if index >= len(sequence) line 12, was without =
# sequence.append(sequence[0]) line 16, was .insert(-1, sequence[0])


