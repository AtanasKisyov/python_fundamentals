data = [int(i) for i in input().split(", ")]
count_of_zeros = data.count(0)
data = [y for y in data if not y == 0]
for zeros in range(count_of_zeros):
    data.append(0)
print(data)
