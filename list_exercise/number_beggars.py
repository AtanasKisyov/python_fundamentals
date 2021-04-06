income = input().split(", ")
beggars = int(input())
offers = 0
result_list = []
nums = []
for n in range(len(income)):
    number = int(income[n])
    nums.append(number)
for i in range(beggars):
    result_list.append(0)
for y in range(len(nums)):
    result_list[offers] += nums[y]
    offers += 1
    if offers == beggars:
        offers = 0
print(result_list)
