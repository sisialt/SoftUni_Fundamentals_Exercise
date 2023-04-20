def calculate_next_number(n):
    tribonacci_sequence = [1, 1, 2]

    if n == 1:
        tribonacci_sequence.pop(-1)
        tribonacci_sequence.pop(-2)
    elif n == 2:
        tribonacci_sequence.pop(-1)
    else:
        for num in range(0, n - 3):
            result = tribonacci_sequence[0 + num] + tribonacci_sequence[1 + num] + tribonacci_sequence[2 + num]
            tribonacci_sequence.append(result)
    return tribonacci_sequence


number = int(input())

print(" ".join([str(x) for x in calculate_next_number(number)]))