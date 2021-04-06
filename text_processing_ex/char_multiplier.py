two_strings = input().split()
first_word = two_strings[0]
second_word = two_strings[1]
result = 0
counter = 0
if len(first_word) > len(second_word):
    for i in range(len(first_word)):
        counter += 1
        if not counter > len(second_word):
            result += ord(first_word[i]) * ord(second_word[i])
        else:
            result += ord(first_word[i])
elif len(first_word) < len(second_word):
    for i in range(len(second_word)):
        counter += 1
        if not counter > len(first_word):
            result += ord(first_word[i]) * ord(second_word[i])
        else:
            result += ord(second_word[i])
else:
    for i in range(len(first_word)):
        result += ord(first_word[i]) * ord(second_word[i])
print(result)
