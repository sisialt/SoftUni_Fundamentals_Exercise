sequence = [int(x) for x in input().split()]
command = input()

count_shot_targets = 0

while command != "End":
    index = int(command)

    if 0 <= index < len(sequence):
        target = sequence[index]

        if target != -1:
            sequence[index] = -1

            for i in range(len(sequence)):
                if sequence[i] != -1:
                    if sequence[i] > target:
                        sequence[i] -= target
                    else:
                        sequence[i] += target

            count_shot_targets += 1

    command = input()

else:
    print(f"Shot targets: {count_shot_targets} -> {' '.join([str(x) for x in sequence])}")

# line 17 after validate index
# change sequence: for-loop with i in range, not seq in sequence
# line 20 should be before for-loop and not after
