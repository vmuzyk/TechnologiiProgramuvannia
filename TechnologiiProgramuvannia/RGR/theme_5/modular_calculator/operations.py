from .functions import add, subtract, multiply, divide

def get_number(prompt):
    """Безпечне отримання числа від користувача."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Помилка! Введіть коректне число.")

def get_operator():
    """Отримання оператора від користувача."""
    while True:
        operator = input("Введіть оператор (+, -, *, /) або 'q' для виходу: ").strip()
        if operator in ['+', '-', '*', '/', 'q']:
            return operator
        print("Невідомий оператор. Спробуйте ще раз.")

def perform_operation(operator, num1, num2):
    """Виконання операції на основі оператора."""
    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide
    }
    
    if operator not in operations:
        raise ValueError("Невідомий оператор")
    
    return operations[operator](num1, num2)