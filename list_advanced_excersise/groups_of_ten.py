nums = input().split(", ")
nums = list(map(lambda x: int(x), nums))
result_list = []
for i in range(10, 100000, 10):
    if len(nums) == 0:
        break
    result_list = [y for y in nums if y <= i]
    nums = [x for x in nums if x > i]
    print(f"Group of {i}'s: {result_list}")
    result_list.clear()
