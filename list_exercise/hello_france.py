article_list = input().split("|")
budget = float(input())
bought_items = []
spent_money = 0
profit = 0
for i in range(len(article_list)):
    item, price = article_list[i].split("->")
    price = float(price)
    if item == "Clothes" and price > 50.00:
        continue
    elif item == "Shoes" and price > 35.00:
        continue
    elif item == "Accessories" and price > 20.50:
        continue
    if budget >= price:
        spent_money += price
        budget -= price
        item_profit = price * 0.40
        profit += item_profit
        bought_items.append(price + item_profit)

for y in bought_items:
    print(f"{y:.2f}", end=' ')
print("")
print(f'Profit: {profit:.2f}')

budget += sum(bought_items)

if budget >= 150:
    print('Hello, France!')
else:
    print('Time to go.')
