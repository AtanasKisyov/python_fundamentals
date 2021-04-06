budget = float(input())
flour_price = float(input())
egg_pack_price = flour_price * 0.75
milk_liter_price = flour_price * 1.25
cozonac_price = egg_pack_price + flour_price + (milk_liter_price * 0.25)
coloured_eggs = 0
counter = 0
while budget - cozonac_price >= 0:
    coloured_eggs += 3
    counter += 1
    if counter % 3 == 0:
        coloured_eggs -= counter - 2
    budget -= cozonac_price

print(f'You made {counter} cozonacs! Now you have {coloured_eggs} eggs and {budget:.2f}BGN left.')
