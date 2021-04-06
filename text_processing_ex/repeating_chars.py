data = input()
new_word = ""
previous_char = ""
for i in data:
    if previous_char == i:
        previous_char = i
        continue
    else:
        new_word += i
        previous_char = i
print(new_word)
