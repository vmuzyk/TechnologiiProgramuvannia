def test_list_methods():
    # Початковий список
    my_list = [1, 2, 3]
    print(f"Початковий список: {my_list}")
    
    # extend()
    my_list.extend([4, 5])
    print(f"Після extend([4, 5]): {my_list}")
    
    # append()
    my_list.append(6)
    print(f"Після append(6): {my_list}")
    
    # insert()
    my_list.insert(2, 99)
    print(f"Після insert(2, 99): {my_list}")
    
    # remove()
    my_list.remove(99)
    print(f"Після remove(99): {my_list}")
    
    # copy()
    list_copy = my_list.copy()
    print(f"Копія списку: {list_copy}")
    
    # reverse()
    my_list.reverse()
    print(f"Після reverse(): {my_list}")
    
    # sort()
    my_list.sort()
    print(f"Після sort(): {my_list}")
    
    # clear()
    my_list.clear()
    print(f"Після clear(): {my_list}")

if __name__ == "__main__":
    test_list_methods()