def find_discriminant(a: float, b: float, c: float) -> float:
   
    return b**2 - 4*a*c

if __name__ == "__main__":
    
    a, b, c = 1, -3, 2
    d = find_discriminant(a, b, c)
    print(f"Дискримінант для {a}x² + {b}x + {c} = {d}")