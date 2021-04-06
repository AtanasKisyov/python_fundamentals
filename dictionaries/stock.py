data = input().split()
products = {}
for i in range(0, len(data), 2):
    key = data[i]
    value = data[i + 1]
    products[key] = int(value)

order = input().split()

for y in order:
    if y in products:
        print(f"We have {products[y]} of {y} left")
    else:
        print(f"Sorry, we don't have {y}")
