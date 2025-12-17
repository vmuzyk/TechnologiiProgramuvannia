def find_insert_position(sorted_list, new_element):
    
    for i, element in enumerate(sorted_list):
        if new_element <= element:
            return i
    return len(sorted_list)

if __name__ == "__main__":
    # Тестування
    sorted_list = [1, 3, 5, 7, 9]
    test_elements = [0, 2, 5, 10]
    
    for element in test_elements:
        position = find_insert_position(sorted_list, element)
        print(f"Для елемента {element} позиція для вставки: {position}")