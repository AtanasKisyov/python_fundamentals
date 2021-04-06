data = input().split()
products = {}

for i in range(0, len(data), 2):
    key = data[i]
    value = data[i + 1]
    products[key] = int(value)

print(products)
