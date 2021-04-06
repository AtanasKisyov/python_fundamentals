data = input()
user = ''
language = ''
soft_uni = {}
storage_language = {}
while "exam finished" not in data:
    if "banned" not in data:
        user, language, points = data.split('-')
        points = int(points)
        if language not in storage_language:
            storage_language[language] = 1
        else:
            storage_language[language] += 1
        if user in soft_uni:
            if soft_uni[user][1] > points:
                data = input()
                continue
            else:
                soft_uni[user][1] = points
        else:
            soft_uni[user] = [language, points]
    else:
        soft_uni['banned'] = soft_uni.pop(user)
    data = input()

soft_uni = dict(sorted(soft_uni.items(), key=lambda x: x[0]))
soft_uni = dict(sorted(soft_uni.items(), key=lambda x: x[1][1], reverse=True))

print("Results:")
for key, value in soft_uni.items():
    if key == 'banned':
        continue
    else:
        print(f"{key} | {value[1]}")
print("Submissions:")

storage_language = dict(sorted(storage_language.items(), key=lambda x: x[0]))
storage_language = dict(sorted(storage_language.items(), key=lambda x: x[1], reverse=True))

for key, value in storage_language.items():
    print(f"{key} - {value}")
