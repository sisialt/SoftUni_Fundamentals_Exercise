population = [int(x) for x in input().split(", ")]
minimum_wealth = int(input())

new_population = population.copy()
total_difference_wealth_to_minimum = 0

for poor in population:
    if poor < minimum_wealth:
        total_difference_wealth_to_minimum += minimum_wealth - poor
        new_population.remove(poor)
        new_population.insert(population.index(poor), minimum_wealth)

wealthiest = max(population)

if wealthiest - total_difference_wealth_to_minimum >= minimum_wealth:
    new_population.insert(population.index(wealthiest), wealthiest - total_difference_wealth_to_minimum)
    new_population.remove(wealthiest)
    print(new_population)

else:
    print("No equal distribution possible")
