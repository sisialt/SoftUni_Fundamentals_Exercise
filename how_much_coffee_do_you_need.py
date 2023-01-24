coffees = 0

while True:
    word = input()

    if word == "END":
        break

    if word == "coding" or word == "cat" or word == "dog" or word == "movie":
        coffees += 1

    if word == "CODING" or word == "CAT" or word == "DOG" or word == "MOVIE":
        coffees += 2

if coffees > 5:
    print("You need extra sleep")
else:
    print(coffees)