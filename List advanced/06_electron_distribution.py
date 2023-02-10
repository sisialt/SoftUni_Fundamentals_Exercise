electrons = int(input())

shells_filled = []

while electrons:
    n = len(shells_filled) + 1
    max_electrons = min(2 * (n ** 2), electrons)
    shells_filled.append(max_electrons)
    electrons -= max_electrons

print(shells_filled)

# left_electrons = electrons
#
# for n in range(1, electrons):
#     max_electrons = 2 * (n ** 2)
#     left_electrons -= max_electrons
#     shells_filled.append(max_electrons)
#
#     if left_electrons <= 2 * ((n + 1) ** 2):
#         shells_filled.append(left_electrons)
#         break
#
# print(shells_filled)



