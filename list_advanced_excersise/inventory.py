inventory = input().split(", ")
command = input()
result = ''
while command != "Craft!":
    action, item = command.split(" - ")
    if action == "Collect":
        if item in inventory:
            command = input()
            continue
        else:
            inventory.append(item)
    elif action == "Drop":
        if item in inventory:
            inventory.remove(item)
    elif action == "Combine Items":
        item1, item2 = item.split(":")
        if item1 in inventory:
            index = inventory.index(item1)
            inventory.insert(index + 1, item2)
    elif action == "Renew":
        if item in inventory:
            inventory.remove(item)
            inventory.append(item)
    command = input()
result = ', '.join([i for i in inventory])
print(result)
