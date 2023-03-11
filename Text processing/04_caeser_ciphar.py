text = input()
encrypted_text = ""

for ch in text:
    encrypted_text += ch.replace(ch, chr(ord(ch) + 3))

print(encrypted_text)