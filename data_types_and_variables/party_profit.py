from math import floor
party_size = int(input())
days = int(input())
daily_coins = 50
total_coins = 0
for i in range(1, days + 1):
    total_coins += daily_coins
    if i % 10 == 0:
        party_size -= 2
    if i % 15 == 0:
        party_size += 5
    if i % 3 == 0:
        total_coins -= 5 * party_size
    else:
        total_coins -= 2 * party_size
    if i % 5 == 0:
        if i % 3 == 0:
            total_coins += 18 * party_size
        else:
            total_coins += 20 * party_size
result = floor(total_coins / party_size)
print(f"{party_size} companions received {result} coins each.")
