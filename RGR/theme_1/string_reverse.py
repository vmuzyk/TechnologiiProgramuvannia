def reverse_string(s: str) -> str:
   
    return s[::-1]


if __name__ == "__main__":
    input_string = "Hello, World!"
    reversed_string = reverse_string(input_string)
    print(f"Оригінал: {input_string}")
    print(f"Реверс: {reversed_string}")