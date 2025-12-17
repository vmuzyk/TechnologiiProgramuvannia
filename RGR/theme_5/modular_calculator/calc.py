from operations import get_number, get_operator, perform_operation

def main():
    print("Модульний калькулятор")
    
    while True:
        operator = get_operator()
        
        if operator == 'q':
            print("Дякуємо за використання калькулятора!")
            break
        
        num1 = get_number("Введіть перше число: ")
        num2 = get_number("Введіть друге число: ")
        
        try:
            result = perform_operation(operator, num1, num2)
            print(f"Результат: {result}")
        except ValueError as e:
            print(f"Помилка: {e}")
        except Exception as e:
            print(f"Неочікувана помилка: {e}")

if __name__ == "__main__":
    main()