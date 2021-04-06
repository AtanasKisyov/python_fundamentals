import re


data = input()

regex = r"(^_|(?<=\s_))[a-zA-Z0-9]+\b"

match = re.findall(regex, data)

print(','.join(match))
