# def fill_shell(left_electrons, n):
#     max_electrons = 2 * (n ** 2)
#     left_electrons -= max_electrons


electrons = int(input())

shells = []
left_electrons = electrons

for n in range(1, electrons):
    max_electrons = 2 * (n ** 2)
    left_electrons -= max_electrons
    shells.append(max_electrons)

    if left_electrons <= 2 * ((n + 1) ** 2):
        shells.append(left_electrons)
        break

print(shells)

