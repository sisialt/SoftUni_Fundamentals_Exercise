text = input().split()

print("\n".join([word for word in text if len(word) % 2 == 0]))


# for i in range(len(text)):
#     if len(text[i]) % 2 == 0:
#         print(text[i])
