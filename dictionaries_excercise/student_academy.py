n = int(input())
students = {}
passing_students = {}
for i in range(n):
    student = input()
    grade = float(input())
    if student not in students:
        students[student] = []
        students[student].append(grade)
    else:
        students[student].append(grade)

for k, v in students.items():
    students[k] = sum(students[k]) / len(students[k])
    if students[k] >= 4.50:
        passing_students[k] = v

passing_students = {key: sum(value) / len(value) for key, value in passing_students.items()}
passing_students = dict(sorted(passing_students.items(), key=lambda x: x[1], reverse=True))

for k in passing_students:
    print(f"{k} -> {passing_students[k]:.2f}")
