n = int(input())

heroes = {}

for _ in range(n):
    line = input().split()
    hero = line[0]
    hit_points = int(line[1])
    mana_points = int(line[2])

    heroes[hero] = {"HP": hit_points, "MP": mana_points}

while True:
    line = input()
    if line == "End":
        break

    line_args = line.split(" - ")
    command = line_args[0]
    hero = line_args[1]

    if command == "CastSpell":
        mp_needed = int(line_args[2])
        spell_name = line_args[3]

        if heroes[hero]["MP"] >= mp_needed:
            heroes[hero]["MP"] -= mp_needed
            print(f"{hero} has successfully cast {spell_name} and now has {heroes[hero]['MP']} MP!")
        else:
            print(f"{hero} does not have enough MP to cast {spell_name}!")

    elif command == "TakeDamage":
        damage = int(line_args[2])
        attacker = line_args[3]

        heroes[hero]["HP"] -= damage

        if heroes[hero]["HP"] > 0:
            print(f"{hero} was hit for {damage} HP by {attacker} and now has {heroes[hero]['HP']} HP left!")
        else:
            heroes.pop(hero)
            print(f"{hero} has been killed by {attacker}!")

    elif command == "Recharge":
        amount = int(line_args[2])

        if heroes[hero]["MP"] + amount > 200:
            amount = 200 - heroes[hero]["MP"]
        heroes[hero]["MP"] += amount
        print(f"{hero} recharged for {amount} MP!")

    elif command == "Heal":
        amount = int(line_args[2])

        if heroes[hero]["HP"] + amount > 100:
            amount = 100 - heroes[hero]["HP"]
        heroes[hero]["HP"] += amount

        print(f"{hero} healed for {amount} HP!")

for hero, values in heroes.items():
    print(f"{hero}\n  HP: {values['HP']}\n  MP: {values['MP']}")
