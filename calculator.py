import math

def calculate(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        if b == 0:
            return "Error: Division by zero"
        else:
            return a / b
    elif operation == '%':
        return a % b
    elif operation == '^':
        return a ** b
    elif operation == 'sqrt':
        if a != 0:  # Проверка на ноль, чтобы избежать деления на ноль
            return b ** (1 / a)
        else:
            return "Error: Cannot calculate root with degree 0"
    elif operation == 'log':
        if a <= 0 or b <= 0:
            return "Error: Logarithm undefined for non-positive values"
        else:
            return math.log(b, a)  # Логарифм числа b по основанию a
    else:
        return "Ошибка ввода"
a = float(input("Введите первое число (основание для логарифма или первое число): "))
b = float(input("Введите второе число (число для операции): "))
operation = input("Введите математический символ (+, -, *, /, %, ^, sqrt, log): ")
result = calculate(a, b, operation)
print(f"Результат: {result}")
