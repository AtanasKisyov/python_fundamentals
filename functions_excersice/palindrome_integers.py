def palindrome_check(numbers_list):
    for i in range(len(numbers_list)):
        current_num = numbers_list[i][:: - 1]
        if current_num == numbers_list[i]:
            print(True)
        else:
            print(False)


integers_list = input().split(", ")
palindrome_check(integers_list)
