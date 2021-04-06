first_word = input()
second_word = input()
new_word = first_word
for i in range(len(first_word)):
    first_part = first_word[(i + 1):]
    second_part = second_word[:(i + 1)]
    if second_part + first_part == new_word:
        continue
    new_word = second_part + first_part
    print(new_word)
