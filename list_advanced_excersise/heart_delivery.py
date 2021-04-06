neighbourhood = input().split("@")
neighbourhood = [int(x) for x in neighbourhood]
command = input().split()
jump = 0
counter = 0
check = []
while "Love!" not in command:
    jump += int(command[1])
    if jump >= len(neighbourhood):
        jump = 0
    neighbourhood[jump] -= 2
    if neighbourhood[jump] <= 0:
        if jump in check:
            print(f"Place {jump} already had Valentine's day.")
        else:
            print(f"Place {jump} has Valentine's day.")
            check.append(jump)
        neighbourhood[jump] = 0
    command = input().split()
print(f"Cupid's last position was {jump}.")
for i in neighbourhood:
    if i > 0:
        counter += 1
if counter > 0:
    print(f'Cupid has failed {counter} places.')
else:
    print("Mission was successful.")
