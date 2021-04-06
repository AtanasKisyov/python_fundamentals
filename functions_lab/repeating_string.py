def concatenate_string(text, n):
    result = ""
    for i in range(0, n):
        result += text
    return result


income = input()
rotations = int(input())
print(concatenate_string(income, rotations))
