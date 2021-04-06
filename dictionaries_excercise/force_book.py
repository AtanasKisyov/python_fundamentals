data = input()
force_side = ''
force_user = ''
force = {}
while "Lumpawaroo" not in data:
    if "|" in data:
        data = data.split(" | ")
        force_side = data[0]
        force_user = data[1]
        if force_user not in force.values():
            force[force_side] = []
            force[force_side].append(force_user)
    elif " -> " in data:
        data = data.split(" -> ")
        force_side = data[1]
        force_user = data[0]
        if force_user in force.values():
            force[force_side].append(force_user)
    data = input()
