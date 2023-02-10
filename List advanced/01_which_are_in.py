sequence1 = input().split(", ")
sequence2 = input().split(", ")

new = []

for seq in sequence1:
    for i in range(len(sequence2)):  # for seq2 in sequence2:  if seq in seq2
        if seq in sequence2[i]:
            new.append(seq)
            break

print(new)

# print([seq for seq in sequence1 if seq in sequence2])
