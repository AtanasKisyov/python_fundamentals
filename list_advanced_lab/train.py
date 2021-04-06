wagons = int(input())
train = [0 for i in range(wagons)]
command = input()

while command != "End":
    if "add" in command:
        add, num = command.split()
        num = int(num)
        train[-1] += num
    elif "insert" in command:
        insert, index, num = command.split()
        num = int(num)
        index = int(index)
        train[index] += num
    elif "leave" in command:
        leave, index, num = command.split()
        num = int(num)
        index = int(index)
        train[index] -= num
    command = input()

print(train)
