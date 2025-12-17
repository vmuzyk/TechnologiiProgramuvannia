def safe_input(prompt, input_type=float):
    
    while True:
        try:
            value = input(prompt)
            if input_type == float:
                return float(value)
            elif input_type == str:
                return value.strip()
        except ValueError:
            print("Помилка! Будь ласка, введіть коректне значення.")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        if b == 0:
            raise ZeroDivisionError("Ділення на нуль неможливе")
        return a / b
    except ZeroDivisionError as e:
        return f"Помилка: {e}"

def calculator_with_exceptions():
    print("Калькулятор з обробкою винятків")
    print("Доступні операції: +, -, *, /")
    print("Для виходу введіть 'q' як оператор")
    
    while True:
        try:
            operator = safe_input("\nВведіть оператор (+, -, *, /) або 'q' для виходу: ", str)
            
            if operator.lower() == 'q':
                print("Дякуємо за використання калькулятора!")
                break
            
            if operator not in ['+', '-', '*', '/']:
                print("Невідомий оператор. Спробуйте ще раз.")
                continue
            
            num1 = safe_input("Введіть перше число: ")
            num2 = safe_input("Введіть друге число: ")
            
            if operator == '+':
                result = add(num1, num2)
            elif operator == '-':
                result = subtract(num1, num2)
            elif operator == '*':
                result = multiply(num1, num2)
            elif operator == '/':
                result = divide(num1, num2)
            
            print(f"Результат: {result}")
            
        except KeyboardInterrupt:
            print("\nПрограма перервана користувачем")
            break
        except Exception as e:
            print(f"Сталася неочікувана помилка: {type(e).__name__}: {e}")

if __name__ == "__main__":
    calculator_with_exceptions()