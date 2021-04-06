import re


numbers = input()

regex = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"

match_nums = re.finditer(regex, numbers)

for n in match_nums:
    print(n.group(0), end=" ")
