n = int(input())
for i in range(0, n):
    for y in range(0, n):
        for u in range(0, n):
            print(f'{chr(97 + i)}{chr(97 + y)}{chr(97 + u)}')
