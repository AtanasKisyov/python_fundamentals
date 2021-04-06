income = input().split()
numbers = []
convert_numbers = []
for i in range(len(income)):
    numbers.append(int(income[i]))
    convert_numbers.append(numbers[i] * -1)
print(convert_numbers)
