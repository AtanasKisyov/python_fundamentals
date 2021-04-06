def factorial_numbers(n1, n2):
    factorial1 = 1
    factorial2 = 1
    for i in range(1, n1 + 1):
        factorial1 *= i
    for y in range(1, n2 + 1):
        factorial2 *= y
    division_result = factorial1 / factorial2
    return division_result


number1 = int(input())
number2 = int(input())
result = factorial_numbers(number1, number2)

print(f'{result:.2f}')
