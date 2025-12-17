def test_string_methods():
    test_string = "  hello world  "
    
    print(f"Оригінал: '{test_string}'")
    print(f"strip(): '{test_string.strip()}'")
    print(f"capitalize(): '{test_string.strip().capitalize()}'")
    print(f"title(): '{test_string.strip().title()}'")
    print(f"upper(): '{test_string.strip().upper()}'")
    print(f"lower(): '{test_string.strip().lower()}'")

if __name__ == "__main__":
    test_string_methods()