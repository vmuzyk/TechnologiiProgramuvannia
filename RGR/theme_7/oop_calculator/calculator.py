class Calculator:
    
    
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def subtract(a, b):
        return a - b
    
    @staticmethod
    def multiply(a, b):
        return a * b
    
    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ValueError("Ділення на нуль неможливе")
        return a / b
    
    @staticmethod
    def power(a, b):
        return a ** b
    
    @staticmethod
    def sqrt(a):
        if a < 0:
            raise ValueError("Квадратний корінь з від'ємного числа неможливий")
        return a ** 0.5
    
    def __str__(self):
        return "Calculator клас з основними математичними операціями"