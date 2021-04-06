electrons = int(input())
shells = []
shell_num = 0
while electrons != 0:
    shell_num += 1
    formula = 2*shell_num**2
    electrons
    if electrons < formula:
        shells.append(electrons)
        break
    else:
        shells.append(formula)
        electrons -= formula
print(shells)
