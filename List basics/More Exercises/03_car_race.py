numbers = [int(x) for x in input().split()]

time_left_car, time_right_car = 0, 0

for time1 in range(0, len(numbers) // 2):
    if numbers[time1] == 0:
        time_left_car *= 0.8
    time_left_car += numbers[time1]

for time2 in range(len(numbers) - 1, len(numbers) // 2, -1):
    if numbers[time2] == 0:
        time_right_car *= 0.8
    time_right_car += numbers[time2]

if time_left_car > time_right_car:
    print(f"The winner is right with total time: {time_right_car:.1f}")
else:
    print(f"The winner is left with total time: {time_left_car:.1f}")

