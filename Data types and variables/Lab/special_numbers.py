n = int(input())

for num in range(1, n + 1):
    num = str(num)

    sum_num = 0

    for i in range(len(num)):
        sum_num += int(num[i])

    if sum_num == 5 or sum_num == 7 or sum_num == 11:
        print(f"{num} -> True")
    else:
        print(f"{num} -> False")
