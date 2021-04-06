data = input().split(" -> ")
companies = {}

while "End" not in data:
    company, employee_id = data[0], data[1]
    if company not in companies:
        companies[company] = []
        companies[company].append(employee_id)
    else:
        if employee_id not in companies[company]:
            companies[company].append(employee_id)
    data = input().split(" -> ")

companies = dict(sorted(companies.items(), key=lambda x: x[0]))

for key, value in companies.items():
    print(key)
    for v in companies[key]:
        print(f"-- {v}")
