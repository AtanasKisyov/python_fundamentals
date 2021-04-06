word = input()
cipher = ""
for i in word:
    character = ord(i) + 3
    cipher += chr(character)
print(cipher)
