command_list = input().split("|")
energy = 100
coins = 100
bankrupt = False
for i in range(len(command_list)):
    task, value = command_list[i].split("-")
    value = int(value)
    if task == "rest":
        if energy + value > 100:
            gained = 100 - energy
        else:
            gained = value
        energy += gained
        print(f'You gained {gained} energy.')
        print(f'Current energy: {energy}.')
    elif task == "order":
        energy -= 30
        if energy < 0:
            energy += 30 + 50
            print("You had to rest!")
            continue
        else:
            coins += value
            print(f'You earned {value} coins.')
    else:
        if coins - value > 0:
            coins -= value
            print(f'You bought {task}.')
        else:
            bankrupt = True
            print(f'Closed! Cannot afford {task}.')
            break
if not bankrupt:
    print(f'Day completed!')
    print(f'Coins: {coins}')
    print(f'Energy: {energy}')
