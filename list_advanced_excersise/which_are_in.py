first_list = input().split(", ")
second_list = input().split(", ")
result_list = []
for i in range(len(first_list)):
    for y in range(len(second_list)):
        word = first_list[i]
        second_word = second_list[y]
        if word in second_word:
            if word in result_list:
                continue
            else:
                result_list.append(word)
print(result_list)
