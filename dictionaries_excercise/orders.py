data = input().split()
products = {}

while "buy" not in data:
    for el in range(0, len(data), 3):
        key = data[el]
        if key not in products:
            value = [float(data[el + 1]), int(data[el + 2])]
            products[key] = value
        else:
            value = [float(data[el + 1]), int(data[el + 2])]
            products[key][0] = value[0]
            products[key][1] = value[1] + products[key][1]
    data = input().split()
for i in products:
    result = [float(y) for y in products[i]]
    total = result[0] * result[1]
    print(f"{i} -> {total:.2f}")
