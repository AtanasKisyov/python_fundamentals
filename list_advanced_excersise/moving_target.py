target_range = input().split()
target_range = [int(x) for x in target_range]
command = input()

while command != "End":
    action, index, value = command.split()
    index = int(index)
    value = int(value)
    if action == "Shoot":
        if len(target_range) > index >= 0:
            target_range[index] -= value
            target_range = [x for x in target_range if x > 0]
    elif action == "Add":
        if index >= len(target_range) or index < 0:
            print("Invalid placement!")
            command = input()
            continue
        else:
            target_range.insert(index, value)
    elif action == "Strike":
        if index + value <= len(target_range) - 1 and index - value >= 0:
            target_range = target_range[0:index - value] + target_range[index + value + 1:]
        else:
            print("Strike missed!")
    command = input()
result = '|'.join([str(i) for i in target_range])
print(result)
