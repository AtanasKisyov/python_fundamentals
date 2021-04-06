n = int(input())
for i in range(1, n + 1):
    result = 0
    num_to_str = str(i)
    for y in range(len(num_to_str)):
        num = int(num_to_str[y])
        result += num
    if result == 5 or result == 7 or result == 11:
        print(f'{i} -> True')
    else:
        print(f'{i} -> False')
