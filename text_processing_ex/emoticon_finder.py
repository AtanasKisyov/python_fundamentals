expression = input()
emoticons = []
for i in range(len(expression)):
    if ":" == expression[i]:
        emo = expression[i] + expression[i + 1]
        emoticons.append(emo)

for y in emoticons:
    print(y)
