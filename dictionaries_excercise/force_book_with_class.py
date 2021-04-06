def change_sides(side, user):
    user_found = False
    user_side = ''
    if side not in force:
        force[side] = []
    for key, value in force.items():
        if user in force[key]:
            user_found = True
            user_side = key
    if user_found:
        force[user_side].remove(user)
        force[side].append(user)
        print(f"{user} joins the {side} side!")
    else:
        force[side].append(user)
        print(f"{user} joins the {side} side!")


def register_user(side, user):
    user_found = False
    if side not in force:
        force[side] = []
    for key, value in force.items():
        if user in force[key]:
            user_found = True
    if not user_found:
        force[side].append(user)


data = input()
force_user = ""
force_side = ""
force = {}

while "Lumpawaroo" not in data:
    if " | " in data:
        force_side, force_user = data.split(" | ")
        register_user(force_side, force_user)
    elif " -> " in data:
        force_user, force_side = data.split(" -> ")
        change_sides(force_side, force_user)
    data = input()

force = dict(sorted(force.items(), key=lambda x: x[0]))

for k, v in force.items():
    if len(force[k]) > 0:
        force[k].sort()
        print(f"Side: {k}, Members: {len(force[k])}")
        for i in range(len(force[k])):
            print(f"! {force[k][i]}")
