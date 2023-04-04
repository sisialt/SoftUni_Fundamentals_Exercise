string = input()
emoticon = ""

for i, ch in enumerate(string):
    if ch == ":" and i + 1 < len(string):
        emoticon = ch + string[i + 1]
        i += 1
        print(emoticon)
