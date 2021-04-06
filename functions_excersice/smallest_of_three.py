def smallest_of_three(num1, num2, num3):
    smallest_number = min(num1, num2, num3)
    return smallest_number


n1 = int(input())
n2 = int(input())
n3 = int(input())
result = smallest_of_three(n1, n2, n3)
print(result)
