
import urllib.request
import json

def get_exchange_rates_simple():
    
    try:
        url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"
        
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode('utf-8'))
        
        rates = {}
        for currency in data:
            code = currency['cc']
            if code in ['USD', 'EUR', 'PLN']:
                rates[code] = currency['rate']
        
        return rates
        
    except:
        
        return {'USD': 37.5, 'EUR': 40.0, 'PLN': 9.0}

def main_simple():
    print("Конвертер валют НБУ")
    print("Підтримувані валюти: USD, EUR, PLN\n")
    
    
    rates = get_exchange_rates_simple()
    
    print("Актуальні курси НБУ:")
    for currency, rate in rates.items():
        print(f"  {currency}: {rate:.2f} UAH")
    print()
    
    while True:
        try:
            
            currency = input("Введіть код валюти (USD, EUR, PLN) або 'q' для виходу: ").upper()
            
            if currency == 'Q':
                print("До побачення!")
                break
            
            if currency not in rates:
                print("Невірна валюта. Спробуйте ще раз.")
                continue
            
            
            amount = float(input(f"Введіть кількість {currency}: "))
            
            
            result = amount * rates[currency]
            
            
            print(f"\nРезультат: {amount} {currency} = {result:.2f} UAH")
            print(f"Курс: 1 {currency} = {rates[currency]:.4f} UAH")
            print("-" * 30)
            
        except ValueError:
            print("Помилка! Введіть коректне число.")
        except KeyboardInterrupt:
            print("\nПрограма перервана.")
            break
        except Exception as e:
            print(f"Помилка: {e}")

if __name__ == "__main__":
    main_simple()