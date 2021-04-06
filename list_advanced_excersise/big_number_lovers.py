nums = input().split()
nums.sort(reverse=True)
result = ''
for i in nums:
    result += i
print(result)
