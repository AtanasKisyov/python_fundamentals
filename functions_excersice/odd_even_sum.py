def odd_even_sum(number):
    odd_sum = 0
    even_sum = 0
    for i in range(len(num_string)):
        current_num = int(num_string[i])
        if current_num % 2 == 0:
            even_sum += current_num
        else:
            odd_sum += current_num
    return odd_sum, even_sum


num_string = input()
summary = list(odd_even_sum(num_string))
print(f'Odd sum = {summary[0]}, Even sum = {summary[1]}')
