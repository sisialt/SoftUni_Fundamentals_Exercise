string1, string2 = input().split()

result = 0

for i in range(max(len(string1), len(string2))):
    if i < min(len(string1), len(string2)):
        result += ord(string1[i]) * ord(string2[i])
    else:
        if len(string1) > len(string2):
            result += ord(string1[i])
        else:
            result += ord(string2[i])

print(result)

# for i in range(min(len(string1), len(string2))):
#     result += ord(string1[i]) * ord(string2[i])
#
# result += sum([ord(char) for char in string1[min(len(string1), len(string2)):]])
# result += sum([ord(char) for char in string2[min(len(string1), len(string2)):]])
