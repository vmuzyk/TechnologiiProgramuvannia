def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    return "Помилка: ділення на нуль"

def calculator_match():
    print("Калькулятор (match версія)")
    print("Доступні операції: +, -, *, /")
    
    try:
        num1 = float(input("Введіть перше число: "))
        operator = input("Введіть оператор (+, -, *, /): ")
        num2 = float(input("Введіть друге число: "))
        
        match operator:
            case '+':
                result = add(num1, num2)
            case '-':
                result = subtract(num1, num2)
            case '*':
                result = multiply(num1, num2)
            case '/':
                result = divide(num1, num2)
            case _:
                result = "Невідомий оператор"
        
        print(f"Результат: {result}")
    except ValueError:
        print("Помилка: некоректне число")

if __name__ == "__main__":
    calculator_match()