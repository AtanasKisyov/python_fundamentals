import re

count_of_messages = int(input())
counter = 0
encrypted_messages = []

for i in range(count_of_messages):
    message = ""
    to_encrypt = input()
    for el in to_encrypt.lower():
        if el.lower() == "s" or el == "t" or el == "a" or el == "r":
            counter += 1
    for el in to_encrypt:
        message += chr(ord(el) - counter)
    encrypted_messages.append(message)
    counter = 0

pattern = r"(?<=@)(?P<planet>[A-Z][a-z]+)[^@\-\!>]+?(?<=\:)(?P<population>[0-9]+(?!\.))[^@\-\:>]*" \
          r"(?<=\!)(?P<type>[AD])(?=\!)[^@:]*\-\>(?P<soldiers>[\d]+)"

planets = {'A': [], 'D': []}

for el in encrypted_messages:
    match_obj = [obj.groupdict() for obj in re.finditer(pattern, el)]
    if match_obj:
        for obj in match_obj:
            if obj['type'] == "A":
                planets['A'].append(obj['planet'])
            elif obj['type'] == "D":
                planets['D'].append(obj['planet'])

planets['A'].sort()
planets['D'].sort()

print(f"Attacked planets: {len(planets['A'])}")
for ap in planets['A']:
    print(f"-> {ap}")
print(f"Destroyed planets: {len(planets['D'])}")
for dp in planets['D']:
    print(f"-> {dp}")
