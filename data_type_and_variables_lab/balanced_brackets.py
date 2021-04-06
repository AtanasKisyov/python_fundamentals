lines = int(input())
opening_bracket = 0
closing_bracket = 0
stack = "(())"
for i in range(lines):
    brackets = input()
    if brackets == "(":
        opening_bracket += 1
        if opening_bracket - closing_bracket > 1:
            print("UNBALANCED")
            break
    elif brackets == ")":
        closing_bracket += 1
        if not (opening_bracket - closing_bracket) == 0:
            print("UNBALANCED")
            break

if opening_bracket == closing_bracket:
    print("BALANCED")
