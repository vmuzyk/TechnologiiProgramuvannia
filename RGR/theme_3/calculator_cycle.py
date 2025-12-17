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

def calculator_cycle():
    print("Калькулятор з циклом")
    print("Доступні операції: +, -, *, /")
    print("Для виходу введіть 'q' як оператор")
    
    while True:
        try:
            operator = input("\nВведіть оператор (+, -, *, /) або 'q' для виходу: ")
            
            if operator.lower() == 'q':
                print("Дякуємо за використання калькулятора!")
                break
            
            if operator not in ['+', '-', '*', '/']:
                print("Невідомий оператор. Спробуйте ще раз.")
                continue
            
            num1 = float(input("Введіть перше число: "))
            num2 = float(input("Введіть друге число: "))
            
            if operator == '+':
                result = add(num1, num2)
            elif operator == '-':
                result = subtract(num1, num2)
            elif operator == '*':
                result = multiply(num1, num2)
            elif operator == '/':
                result = divide(num1, num2)
            
            print(f"Результат: {result}")
            
        except ValueError:
            print("Помилка: некоректне число")
        except Exception as e:
            print(f"Сталася помилка: {e}")

if __name__ == "__main__":
    calculator_cycle()