cards = input()
list_cards = cards.split()

team_a_cards = []
team_b_cards = []
is_terminated = False

for card in list_cards:
    if card in team_a_cards or card in team_b_cards:
        continue
    if "A" in card:
        team_a_cards.append(card)
    elif "B" in card:
        team_b_cards.append(card)

    if len(team_a_cards) > 4 or len(team_b_cards) > 4:
        is_terminated = True
        break

print(f"Team A - {11 - len(team_a_cards)}; Team B - {11 - len(team_b_cards)}")

if is_terminated:
    print(f"Game was terminated")

