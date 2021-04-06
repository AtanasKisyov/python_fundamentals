import re

data = input()

pattern = r"(^|(?<=\s))w{3}\.[a-zA-Z0-9-]+(\.[a-z]+)+($|(?=\s))"

while data:
    match = re.finditer(pattern, data)
    for el in match:
        print(el.group())
    data = input()
