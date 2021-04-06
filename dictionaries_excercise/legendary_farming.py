inventory = {'motes': 0, 'shards': 0, 'fragments': 0}
item = ""
item_material = ""
item_found = False

while not item_found:
    data = [i.lower() for i in input().split()]
    for i in range(0, len(data), 2):
        value = int(data[i])
        key = data[i + 1]
        if key not in inventory:
            inventory[key] = value
            if inventory['motes'] >= 250 or inventory['shards'] >= 250 or inventory['fragments'] >= 250:
                inventory[key] -= 250
                item_material = key
                item_found = True
                break
        else:
            inventory[key] += value
            if inventory['motes'] >= 250 or inventory['shards'] >= 250 or inventory['fragments'] >= 250:
                inventory[key] -= 250
                item_material = key
                item_found = True
                break
        if item_found:
            break


if item_material == "motes":
    item = "Dragonwrath"
elif item_material == "fragments":
    item = "Valanyr"
elif item_material == "shards":
    item = "Shadowmourne"

junk_inventory = {}
cool_inventory = {}

for junk, value in inventory.items():
    if junk == "motes" or junk == "shards" or junk == "fragments":
        continue
    else:
        junk_inventory[junk] = value

for cool, value in inventory.items():
    if cool == "motes" or cool == "shards" or cool == "fragments":
        cool_inventory[cool] = value

junk_inventory = dict(sorted(junk_inventory.items(), key=lambda x: x[0]))
cool_inventory = dict(sorted(cool_inventory.items(), key=lambda x: x[0]))
cool_inventory = dict(sorted(cool_inventory.items(), key=lambda x: x[1], reverse=True))

print(f"{item} obtained!")
for key, value in cool_inventory.items():
    print(f"{key}: {value}")
for key, value in junk_inventory.items():
    print(f"{key}: {value}")
