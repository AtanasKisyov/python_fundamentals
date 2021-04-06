string_list = [i for i in input().split()]

for y in string_list:
    print(f"{y * len(y)}", end="")
