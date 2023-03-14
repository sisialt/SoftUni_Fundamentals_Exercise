def is_winning_ticket(half, count, match_symbol=""):
    max_count = 0
    for i in range(len(half)):
        if half[i] in symbols:
            if half[i] == half[i - 1]:
                count += 1
                if count >= 6:
                    match_symbol = half[i]
                    max_count = count
            else:
                count = 1

    return max_count, match_symbol


input_data = input().split(", ")
symbols = ["@", "#", "$", "^"]

for ticket in input_data:
    ticket = ticket.strip()

    if len(ticket) != 20:
        print(f"invalid ticket")
        continue

    first_half = ticket[:len(ticket) // 2]
    second_half = ticket[len(ticket) // 2:]
    count_1, count_2 = 0, 0

    count_1, match_symbol_1 = is_winning_ticket(first_half, count_1)
    count_2, match_symbol_2 = is_winning_ticket(second_half, count_2)

    if count_1 >= 10 and count_2 >= 10 and match_symbol_1 == match_symbol_2:
        print(f'ticket "{ticket}" - {min(count_1, count_2)}{match_symbol_1} Jackpot!')
    elif count_1 >= 6 and count_2 >= 6 and match_symbol_1 == match_symbol_2:
        print(f'ticket "{ticket}" - {min(count_1, count_2)}{match_symbol_1}')
    else:
        print(f'ticket "{ticket}" - no match')


# line 20: strip() returns result


# def get_char_best_result(half, char):
#     max_count = 0
#     count = 0
#     for ch in half:
#         if ch == char:
#             count += 1
#         else:
#             max_count = max(max_count, count)
#             count = 0
#
#     return max(max_count, count)
#
#
# tickets = [ticket.strip() for ticket in input().split(", ")]
# symbols = ["@", "#", "$", "^"]
#
# for ticket in tickets:
#
#     if len(ticket) != 20:
#         print(f"invalid ticket")
#         continue
#
#     first_half = ticket[:10]
#     second_half = ticket[10:]
#
#     max_count = 0
#     best_symbol = ""
#     for symbol in symbols:
#         first_half_score = get_char_best_result(first_half, symbol)
#         second_half_score = get_char_best_result(second_half, symbol)
#         overall_result = min(first_half_score, second_half_score)
#
#         if overall_result > max_count:
#             max_count = overall_result
#             best_symbol = symbol
#
#     if max_count == 10:
#         print(f'ticket "{ticket}" - {max_count}{best_symbol} Jackpot!')
#     elif max_count >= 6:
#         print(f'ticket "{ticket}" - {max_count}{best_symbol}')
#     else:
#         print(f'ticket "{ticket}" - no match')
#
#
