version = input().split(".")
version = list(map(lambda x: int(x), version))
first, second, third = version[0], version[1], version[2]
num = first * 100 + second * 10 + third + 1
result = str(num)
print(f'{result[0]}.{result[1]}.{result[2]}')
