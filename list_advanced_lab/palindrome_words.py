command = input().split()
searched_palindrome = input()
palindromes = []

for word in range(len(command)):
    if command[word] == command[word][::-1]:
        palindromes.append(command[word])
print(palindromes)
print(f'Found palindrome {palindromes.count(searched_palindrome)} times')
