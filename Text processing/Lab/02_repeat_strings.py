input_data = input().split()

result = ""

for word in input_data:
    result += word * len(word)

print(result)
