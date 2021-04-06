d = int(input())
b = int(input())
all_numbers = []

for i in range(1, b + 1):
    if i % d == 0:
        all_numbers.append(i)
print(max(all_numbers))
