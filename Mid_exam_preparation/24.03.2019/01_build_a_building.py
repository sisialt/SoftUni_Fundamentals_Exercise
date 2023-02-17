budget = float(input())
initial_capital = float(input())
investors = int(input())

money_received = 0

for i in range(1, investors + 1):
    money = float(input())
    money_received += money
    print(f"Investor {i} gave us {money:.2f}.")

    if money_received + initial_capital >= budget:
        print(f"We will manage to build it. Start now! Extra money - {money_received + initial_capital - budget:.2f}.")
        break

else:
    print(f"Project can not start. We need {budget - (money_received + initial_capital):.2f} more.")
