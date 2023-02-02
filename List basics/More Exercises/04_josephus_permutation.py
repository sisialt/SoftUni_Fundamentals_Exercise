numbers = [int(x) for x in input().split()]
k = int(input())

loop_counter = 0
executed = []
index = 0

while len(numbers) > 0:
    loop_counter += 1
    if loop_counter % k == 0:
        executed.append(numbers[index])
        numbers.pop(index)
    else:
        index += 1

    if index >= len(numbers):
        index = 0

print(str(executed).replace(' ', ''))
