



# ace, two, three, four, five, six
# ace, four, two, five, three, six
# 0, 1, 2, 3, 4, 5, 6, 7    4, 2, 3, 1, 5, 6    4, 5, 3, 1, 2, 6   4, 5, 6, 1, 2, 3
# 0, 4, 1, 5, 2, 6, 3, 7

cards = input().split()
shuffles_count = int(input())
shuffled_cards = cards
result = [] * len(cards)

for _ in range(shuffles_count):
    while len(shuffled_cards) > 4:
        for i in range(0, len(shuffled_cards) // 2 - 1):
            shuffled_cards[1 + i], shuffled_cards[len(shuffled_cards) // 2 + i] = \
                shuffled_cards[len(shuffled_cards) // 2 + i], shuffled_cards[1 + i]
            # cards[1 + 1], cards[len(cards) // 2 + 1] = cards[len(cards) // 2 + 1], cards[1 + 1]
            # cards[1 + 2], cards[len(cards) // 2 + 2] = cards[len(cards) // 2 + 2], cards[1 + 2]
        result.insert(len(shuffled_cards) - 1, shuffled_cards[len(shuffled_cards) - 1])
        result.insert(0, shuffled_cards[0])
        shuffled_cards.pop(len(shuffled_cards) - 1)
        shuffled_cards.pop(0)

cards[1 + 1], cards[len(cards) // 2] = cards[len(cards) // 2], cards[1 + 1]

#cards[2], cards[2] = cards[4], cards[3]
print(cards)
print(shuffled_cards)
print(result)


