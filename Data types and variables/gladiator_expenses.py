lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

expenses = 0
shield_breaks_count = 0

for i in range(1, lost_fights_count + 1):
    if i % 2 == 0:
        expenses += helmet_price

    if i % 3 == 0:
        expenses += sword_price

    if i % 6 == 0:
        expenses += shield_price
        shield_breaks_count += 1

        if shield_breaks_count % 2 == 0 and shield_breaks_count != 0:
            expenses += armor_price

print(f"Gladiator expenses: {expenses:.2f} aureus")
