command = input()
statistic = {}
while not command == "statistics":
    key, value = command.split(": ")
    if key in statistic:
        statistic[key] += int(value)
    else:
        statistic[key] = int(value)
    command = input()
print("Products in stock:")
for i in statistic:
    print(f" - {i}: {statistic[i]}")
print(f"Total Products: {len(statistic.keys())}")
print(f"Total Quantity: {sum(statistic.values())}")
