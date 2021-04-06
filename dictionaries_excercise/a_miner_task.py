resource = input()

total_resources = {}
while not resource == "stop":
    quantity = int(input())
    if resource not in total_resources:
        total_resources[resource] = quantity
    else:
        total_resources[resource] += quantity
    resource = input()

for r in total_resources:
    print(f"{r} -> {total_resources[r]}")
