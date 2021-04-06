nums = input().split()
n = int(input())
nums = [int(i) for i in nums]
for y in range(n):
    nums.remove(min(nums))
print(nums)
