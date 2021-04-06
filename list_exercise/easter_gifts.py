gifts = input().split()
command = input()

while command != "No Money":
    command = command.split()
    if "OutOfStock" in command:
        remove_item = command[1]
        for i in range(len(gifts)):
            if remove_item == gifts[i]:
                gifts.insert(i, "None")
                gifts.remove(remove_item)
    elif "Required" in command:
        remove_insert_index = int(command[2])
        if remove_insert_index >= len(gifts):
            command = input()
            continue
        remove_element = gifts[remove_insert_index]
        insert_element = command[1]
        gifts.remove(remove_element)
        gifts.insert(remove_insert_index, insert_element)
    elif "JustInCase" in command:
        gifts.pop()
        gifts.append(command[1])
    command = input()
while "None" in gifts:
    gifts.remove("None")
print(*gifts)
