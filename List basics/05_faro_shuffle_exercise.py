cards = input().split()
counter = int(input())

for _ in range(counter):
    first_half, second_half = [], []
    shuffled = []
    first_half_index, second_half_index = 0, 0

    for i in range(1, len(cards) - 1):
        card = cards[i]
        if i < len(cards) / 2:
            first_half.append(card)
        else:
            second_half.append(card)

    for i in range(len(first_half) * 2):
        if i % 2 == 0:
            shuffled.append(second_half[second_half_index])
            second_half_index += 1
        else:
            shuffled.append(first_half[first_half_index])
            first_half_index += 1

    cards = [cards[0]] + shuffled + [cards[-1]]

print(cards)