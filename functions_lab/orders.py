def orders(prod, qty):
    result = 0
    if prod == "coffee":
        result = qty * 1.50
    elif prod == "water":
        result = qty
    elif prod == "coke":
        result = qty * 1.40
    elif prod == "snacks":
        result = qty * 2
    return result


product = input()
quantity = int(input())
bill = orders(product, quantity)
print(f'{bill:.2f}')
