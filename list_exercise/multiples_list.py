factor = int(input())
count = int(input())
multiples_list = []

for i in range(factor, factor * count + 1, factor):
    multiples_list.append(i)
print(multiples_list)
