def perfect_number(num):
    positive_divisors = []
    is_perfect = False
    for i in range(1, num):
        if num % i == 0:
            positive_divisors.append(i)
    if sum(positive_divisors) == num:
        is_perfect = True
    else:
        is_perfect = False
    return is_perfect


number = int(input())
result = perfect_number(number)

if result:
    print("We have a perfect number!")
else:
    print("It's not so perfect.")
