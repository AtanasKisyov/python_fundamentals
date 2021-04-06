banned_words = [i for i in input().split(", ")]
string = input()

for y in banned_words:
    string = string.replace(y, "*" * len(y))

print(string)
