def simple_calculations(operator, num1, num2):
    result = None
    if operator == "multiply":
        result = num1 * num2
    elif operator == "divide":
        result = int(num1 / num2)
    elif operator == "subtract":
        result = num1 - num2
    elif operator == "add":
        result = num1 + num2
    return result


operation = input()
number1 = int(input())
number2 = int(input())
print(simple_calculations(operation, number1, number2))
