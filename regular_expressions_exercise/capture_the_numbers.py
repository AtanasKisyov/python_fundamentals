import re


data = input()

regex = r"\d+"

result = []

while data:
    match = re.findall(regex, data)
    if match:
        result.extend(match)
    data = input()

print(*result)
