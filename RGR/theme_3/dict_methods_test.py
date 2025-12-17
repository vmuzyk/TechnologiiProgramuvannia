def test_dict_methods():
    # Початковий словник
    my_dict = {'name': 'John', 'age': 25}
    print(f"Початковий словник: {my_dict}")
    
    # update()
    my_dict.update({'city': 'Kyiv', 'age': 26})
    print(f"Після update({{'city': 'Kyiv', 'age': 26}}): {my_dict}")
    
    # keys()
    print(f"Ключі: {list(my_dict.keys())}")
    
    # values()
    print(f"Значення: {list(my_dict.values())}")
    
    # items()
    print(f"Пари ключ-значення: {list(my_dict.items())}")
    
    # del
    del my_dict['city']
    print(f"Після del my_dict['city']: {my_dict}")
    
    # clear()
    my_dict.clear()
    print(f"Після clear(): {my_dict}")

if __name__ == "__main__":
    test_dict_methods()