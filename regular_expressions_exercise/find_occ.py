import re


data = input().lower()

search_word = input().lower()

regex = fr"\b{search_word}\b"

result = re.findall(regex, data)

print(len(result))
