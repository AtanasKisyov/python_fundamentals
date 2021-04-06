data = input().split()
result = 0

for element in data:
    res1 = 0
    res2 = 0
    first_letter = element[0]
    last_letter = element[-1]
    num = float(element[1:-1])
    if first_letter.islower():
        first_letter_position = ord(first_letter) - 96
        res1 = num * first_letter_position
    elif first_letter.isupper():
        first_letter_position = ord(first_letter) - 64
        res1 = num / first_letter_position
    if last_letter.islower():
        last_letter_position = ord(last_letter) - 96
        res2 = res1 + last_letter_position
    elif last_letter.isupper():
        last_letter_position = ord(last_letter) - 64
        res2 = res1 - last_letter_position
    result += res2
result = round(result, 2)
print(f"{result:.2f}")
