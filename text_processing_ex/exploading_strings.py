data = input()
result = ''
i = 0
explosion_power = 0
is_exploding = False
while i < len(data):
    if explosion_power == 0:
        is_exploding = False
    if not data[i] == ">":
        if is_exploding and data[i] == ">":
            explosion_power += int(data[i + 1])
            i += 1
            continue
        elif is_exploding and not data[i] == ">":
            explosion_power -= 1
            i += 1
            continue
        else:
            result += data[i]
        i += 1
    else:
        result += data[i]
        explosion_power += int(data[i + 1])
        i += 1
        is_exploding = True
print(result)
