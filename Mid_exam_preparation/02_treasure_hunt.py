treasure = input().split("|")
stolen_items = []

while True:
    line = input()
    if line == "Yohoho!":
        break

    line_args = line.split()
    action = line_args[0]

    if action == "Loot":
        for i in range(1, len(line_args)):
            if line_args[i] not in treasure:
                treasure.insert(0, line_args[i])

    elif action == "Drop":
        index = int(line_args[1])
        if 0 <= index < len(treasure):
            treasure.append(treasure.pop(index))

    elif action == "Steal":
        count = min(int(line_args[1]), len(treasure))
        stolen_items = treasure[-count:]
        treasure = treasure[:-count]
        print(", ".join(stolen_items))

if len(treasure):
    gain = [len(x) for x in treasure]
    average_gain = sum(gain) / len(treasure)
    print(f"Average treasure gain: {average_gain:.2f} pirate credits.")
else:
    print("Failed treasure hunt.")

# line 24, 25 does not function always with this: for i in range(count, 0, -1):
#                                                     stolen_items.append(treasure.pop(-i))
# forgot line 23


