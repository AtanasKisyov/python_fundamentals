data = [i.lower() for i in input().split()]
occurrences = {}

for i in data:
    if i not in occurrences:
        occurrences[i] = data.count(i)

for key, value in occurrences.items():
    if not value % 2 == 0:
        print(key, end=' ')
