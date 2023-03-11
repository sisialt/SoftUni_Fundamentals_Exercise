string = input()
emoticon = ""

for i, ch in enumerate(string):
    if ch == ":":
        emoticon = ch + string[i + 1]
        print(emoticon)
