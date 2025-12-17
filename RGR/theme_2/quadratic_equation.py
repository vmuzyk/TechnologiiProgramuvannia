from theme_1.discriminant import find_discriminant

def solve_quadratic(a: float, b: float, c: float):
   
    if a == 0:
        return "Це не квадратне рівняння (a = 0)"
    
    d = find_discriminant(a, b, c)
    
    if d > 0:
        x1 = (-b + d**0.5) / (2*a)
        x2 = (-b - d**0.5) / (2*a)
        return f"Два різних корені: x1 = {x1:.2f}, x2 = {x2:.2f}"
    elif d == 0:
        x = -b / (2*a)
        return f"Один подвійний корінь: x = {x:.2f}"
    else:
        real = -b / (2*a)
        imag = abs(d)**0.5 / (2*a)
        return f"Комплексні корені: {real:.2f} ± {imag:.2f}i"

if __name__ == "__main__":
    
    test_cases = [(1, -3, 2), (1, -4, 4), (1, 2, 5)]
    
    for a, b, c in test_cases:
        print(f"Рівняння: {a}x² + {b}x + {c}")
        print(f"Результат: {solve_quadratic(a, b, c)}\n")