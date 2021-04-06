cards = input().split()
shuffles = int(input())
top_card = cards[0]
bottom_card = cards[-1]
new_deck = []
for s in range(shuffles):
    half = len(cards) // 2
    left_deck = cards[1:half]
    right_deck = cards[half:len(cards) - 1]
    new_deck = []
    for i in range(len(left_deck)):
        new_deck.append(right_deck[i])
        new_deck.append(left_deck[i])
    cards = new_deck.copy()
    cards.insert(0, top_card)
    cards.insert(len(cards), bottom_card)
print(cards)
