data = input().lower()
unique_items = []
string = ''
result = ''
i = 0
while i < len(data):
    el = data[i]
    if el.isdigit():
        num = ''
        while el.isdigit() and i < len(data):
            num += el
            i += 1
            if i >= len(data):
                break
            el = data[i]
        result += string * int(num)
        string = ''
    else:
        if el not in unique_items:
            unique_items.append(el)
        string += el.upper()
        i += 1


print(f"Unique symbols used: {len(set(result))}")
print(result)
