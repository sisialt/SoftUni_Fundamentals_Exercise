import re

books = {}

while True:
    line = input()
    if line == "on work":
        break

    pattern = r"^([A-Za-z\d]+) ([A-Za-z\d]+) ((0|[1-9][0-9]*)(\.\d+)?) \-\> (([A-Za-z]+, )*)([A-Za-z]+)$"

    matches = re.findall(pattern, line)

    if not matches:
        continue

    for match in matches:
        title_of_book = match[0]
        author = match[1]
        price = float(match[2])
        chapters = (match[5] + match[7]).split(", ")

        books[title_of_book] = {"Author": author, "Price": price, "Chapters": chapters}

sold_books = []

while True:
    title = input()
    if title == "end work":
        break

    if title not in books:
        print(f"No such book here")
        continue

    sold_books.append(title)
    sold_books.append(books[title])

if not sold_books:
    print(f"Bad day :(")
else:
    total_price_sold_books = 0
    for i in range(0, len(sold_books), 2):
        values = sold_books[i + 1]
        book_title = sold_books[i]

        print(f"SOLD: {book_title} with author {values['Author']}. Chapters in the book {len(values['Chapters'])}")
        total_price_sold_books += values['Price']

    print(f"Money: {total_price_sold_books:.2f}")

# wrong tests in judge
