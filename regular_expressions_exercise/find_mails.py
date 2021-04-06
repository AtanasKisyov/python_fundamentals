import re


data = input()

regex = r"(^|(?<=\s))[a-zA-Z0-9]+[\._-]?[a-zA-Z0-9]+@[A-Za-z]+\-?[A-Za-z]+(\.[A-Za-z]+[\-]?[\.]?[A-Za-z]+)+"

result = re.finditer(regex, data)

for mail in result:
    print(mail.group())
