string = input()

occurrences = {}

for el in string:
    if not ord(el) == 32:
        if el not in occurrences:
            occurrences[el] = string.count(el)

for i in occurrences:
    print(f"{i} -> {occurrences[i]}")
