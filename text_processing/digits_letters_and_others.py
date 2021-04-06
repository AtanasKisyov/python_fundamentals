digits = []
letters = []
others = []

string = input()

for i in string:
    if i.isdigit():
        digits.append(i)
    elif i.isalpha():
        letters.append(i)
    else:
        others.append(i)

print(f"{''.join(digits)}")
print(f"{''.join(letters)}")
print(f"{''.join(others)}")
