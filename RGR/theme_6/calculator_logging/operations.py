import logging

from functions import add, subtract, multiply, divide


logging.basicConfig(
    filename='calculator.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def log_operation(operator, num1, num2, result):
    """Логування операції."""
    logging.info(f"Operation: {num1} {operator} {num2} = {result}")

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Помилка! Введіть коректне число.")

def get_operator():
    while True:
        operator = input("Введіть оператор (+, -, *, /) або 'q' для виходу: ").strip()
        if operator in ['+', '-', '*', '/', 'q']:
            return operator
        print("Невідомий оператор. Спробуйте ще раз.")

def perform_operation(operator, num1, num2):
    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide
    }
    
    if operator not in operations:
        raise ValueError("Невідомий оператор")
    
    result = operations[operator](num1, num2)
    log_operation(operator, num1, num2, result)
    return result