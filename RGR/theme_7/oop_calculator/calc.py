from operations import CalculatorOperations

def main():
    print("ООП Калькулятор з розширеними функціями")
    print("Доступні операції: +, -, *, /, ^ (піднесення до степеня), sqrt (квадратний корінь)")
    
    calculator = CalculatorOperations()
    
    while True:
        operator = calculator.get_operator()
        
        if operator == 'q':
            print("Дякуємо за використання калькулятора!")
            break
        
        try:
            result = calculator.perform_operation(operator)
            print(f"Результат: {result}")
        except ValueError as e:
            print(f"Помилка: {e}")
        except Exception as e:
            print(f"Неочікувана помилка: {type(e).__name__}: {e}")

if __name__ == "__main__":
    main()