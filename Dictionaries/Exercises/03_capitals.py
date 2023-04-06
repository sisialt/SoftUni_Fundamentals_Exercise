countries = input().split(", ")
capitals = input().split(", ")

result = dict(zip(countries, capitals))
# result = {countries[i]: capitals[i] for i in range(len(countries))}

for country, capital in result.items():
    print(f"{country} -> {capital}")
