import logging
from calculator import Calculator

class CalculatorOperations:
    
    
    def __init__(self, log_file='calculator_oop.log'):
        self.calc = Calculator()
        self.setup_logging(log_file)
    
    def setup_logging(self, log_file):
        
        logging.basicConfig(
            filename=log_file,
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
    
    def log_operation(self, operation, *args, result):
        
        logging.info(f"{operation}: {args} = {result}")
    
    def get_number(self, prompt):
        
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Помилка! Введіть коректне число.")
    
    def get_operator(self):
        
        operators = ['+', '-', '*', '/', '^', 'sqrt', 'q']
        while True:
            operator = input(f"Введіть оператор ({', '.join(operators)}) або 'q' для виходу: ").strip()
            if operator in operators:
                return operator
            print("Невідомий оператор. Спробуйте ще раз.")
    
    def perform_operation(self, operator):
        
        operations = {
            '+': (self.calc.add, 2),
            '-': (self.calc.subtract, 2),
            '*': (self.calc.multiply, 2),
            '/': (self.calc.divide, 2),
            '^': (self.calc.power, 2),
            'sqrt': (self.calc.sqrt, 1)
        }
        
        if operator not in operations:
            raise ValueError("Невідомий оператор")
        
        func, num_args = operations[operator]
        
        if num_args == 1:
            num1 = self.get_number("Введіть число: ")
            result = func(num1)
            self.log_operation(operator, num1, result=result)
            return result
        else:
            num1 = self.get_number("Введіть перше число: ")
            num2 = self.get_number("Введіть друге число: ")
            result = func(num1, num2)
            self.log_operation(operator, num1, num2, result=result)
            return result