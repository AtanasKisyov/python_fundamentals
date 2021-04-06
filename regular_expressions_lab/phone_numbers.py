import re

numbers = input()

pattern = r"\+359(?P<sep>\s|-)2(?P=sep)[0-9]{3}(?P=sep)[0-9]{4}\b"

matches = re.findall(pattern, numbers)

print(matches)


#(\+359(\s|-)2\1[0-9]{3}\1[0-9]{4})\b