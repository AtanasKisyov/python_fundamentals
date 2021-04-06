from re import findall

tickets = [ticket.strip() for ticket in input().split(", ")]

win = r"[\^]{6,10}|[\$]{6,10}|[\@]{6,10}|[\#]{6,10}"
jackpot = r"[\^]{20}|[\$]{20}|[\@]{20}|[\#]{20}"

for y in tickets:
    if not len(y) == 20:
        print("invalid ticket")
        continue
    else:
        first_half = y[:10]
        second_half = y[10:]
        check_win_first = findall(win, first_half)
        check_win_second = findall(win, second_half)
        check_jackpot = findall(jackpot, y)
        if check_jackpot:
            print(f"ticket \"{y}\" - 10{y[0]} Jackpot!")
        elif check_win_first and check_win_second:
            lenght = min(len(check_win_first[0]), len(check_win_second[0]))
            print(f"ticket \"{y}\" - {lenght}{check_win_first[0][0]}")
        else:
            print(f"ticket \"{y}\" - no match")
