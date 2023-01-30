string = input().split(", ")

for i in range(0, len(string)):
    if string[i] == "wolf":
        if i == len(string) - 1:
            print("Please go away and stop eating my sheep")
        else:
            print(f"Oi! Sheep number {len(string) - (i + 1)}! You are about to be eaten by a wolf!")
