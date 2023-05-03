numbers = input().split()
text = list(input())

result = ""

for number in numbers:
    sum_num = 0
    for i in range(0, len(number)):
        sum_num += int(number[i])
        if sum_num > len(text):
            sum_num -= len(text)

    result += text[sum_num]
    text.pop(sum_num)

print(result)