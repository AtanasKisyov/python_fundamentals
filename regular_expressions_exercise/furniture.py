import re

data = input()

regex = r"(^>>)(?P<type>[a-zA-Z]+)<<(?P<price>\d+(\.\d+)?)!(?P<qty>\d+)"

total_bought = []

total_price = 0

while not data == "Purchase":
    match = re.match(regex, data)
    if match:
        obj = match.groupdict()
        total_bought.extend([obj['type']])
        total_price += float(obj['price']) * int(obj['qty'])
    data = input()

print("Bought furniture:")

for el in total_bought:
    print(el)

print(f"Total money spend: {total_price:.2f}")
