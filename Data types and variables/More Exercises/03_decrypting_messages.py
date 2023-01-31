key = int(input())
n = int(input())

decrypted_message = []

for _ in range(n):
    letter = input()
    result = ord(letter) + key
    decrypted_message.append(chr(result))

print("".join(decrypted_message))