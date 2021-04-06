key = int(input())
n = int(input())
UPPER_RANGE = range(65, 91)
LOWER_RANGE = range(97, 123)
word = ''
for i in range(n):
    char = ord(input()) + key
    word += chr(char)
print(word)
