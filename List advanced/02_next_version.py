version = [int(x) for x in input().split(".")]

for i in range(-1, -len(version) - 1, -1):
    if version[i] < 9:
        version[i] += 1
        break
    else:
        version[i] = 0

print(".".join(str(x) for x in version))

# if version[-1] < 9:
#     version[-1] += 1
# else:
#     version[-1] = 0
#     if version[-2] < 9:
#         version[-2] += 1
#     else:
#         version[-2] = 0
#         version[-3] += 1
