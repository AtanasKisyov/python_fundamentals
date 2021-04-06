cards_input = input().split()
team_a = [int(a) for a in range(1, 12)]
team_b = [int(b) for b in range(1, 12)]

for i in range(len(cards_input)):
    current = cards_input[i].split("-")
    if "A" in current:
        if int(current[1]) in team_a:
            team_a.remove(int(current[1]))
    elif "B" in current:
        if int(current[1]) in team_b:
            team_b.remove(int(current[1]))
    if len(team_a) < 7 or len(team_b) < 7:
        break
print(f'Team A - {len(team_a)}; Team B - {len(team_b)}')
if len(team_a) < 7 or len(team_b) < 7:
    print('Game was terminated')
