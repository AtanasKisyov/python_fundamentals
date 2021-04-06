command = input()
todo_list = [0 for i in range(10)]
while command != "End":
    items = command.split("-")
    priority = int(items[0]) - 1
    job = items[1]
    todo_list.insert(priority, job)
    command = input()
while 0 in todo_list:
    todo_list.remove(0)
print(todo_list)
