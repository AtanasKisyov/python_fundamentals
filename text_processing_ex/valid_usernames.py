user_names = [i for i in input().split(", ")]
valid_user_names = []
is_valid = True
for y in user_names:
    for z in y:
        if not z.isdigit() and not z.isalpha() and not z == "_" and not z == "-":
            is_valid = False
    if not 3 <= len(y) <= 16:
        is_valid = False
    if is_valid:
        valid_user_names.append(y)
    is_valid = True

for el in valid_user_names:
    print(el)
