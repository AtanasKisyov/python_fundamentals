expression = input().split()
word = []
nums = []
num = ''
result = []
for i in range(len(expression)):
    current_word = expression[i]
    word = [x for x in current_word if not x.isdigit()]
    nums = [x for x in current_word if x.isdigit()]
    word[0], word[-1] = word[-1], word[0]
    for n in nums:
        num += n
    num = chr(int(num))
    word.insert(0, num)
    words = ''.join([str(i) for i in word])
    result.append(words)
    num = ''
print(*result)
