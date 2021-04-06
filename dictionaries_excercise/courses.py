data = input().split(" : ")
courses = {}
while "end" not in data:
    if data[0] not in courses:
        courses[data[0]] = []
        courses[data[0]].append(data[1])
    else:
        courses[data[0]].append(data[1])
    data = input().split(" : ")

courses = dict(sorted(courses.items(), key=lambda x: len(x[1]), reverse=True))


for key, value in courses.items():
    print(f"{key}: {len(courses[key])}")
    value.sort()
    for v in value:
        print(f"-- {v}")
