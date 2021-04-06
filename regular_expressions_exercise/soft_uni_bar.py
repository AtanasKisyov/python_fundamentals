import re

data = input()

regex = r"^%(?P<name>[A-Z][a-z]+)%([^\|\$\%\.]+)?<(?P<product>\w+)>([^\|\$\%\.]+)?\|" \
        r"(?P<count>\d+)\|([^\|\$\%\.0-9]+)?(?P<price>(\d+|(\d+\.\d+)))(?=\$)"

total_income = 0

while not data == "end of shift":
    order = [obj.groupdict() for obj in re.finditer(regex, data)]
    if order:
        total_income += int(order[0]['count']) * float(order[0]['price'])
        print(f"{order[0]['name']}: {order[0]['product']} - {int(order[0]['count']) * float(order[0]['price']):.2f}")
    data = input()

print(f"Total income: {total_income:.2f}")
