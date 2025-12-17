class Student:
    def __init__(self, name, age, grade):
        
        self.name = name
        self.age = age
        self.grade = grade
    
    def __str__(self):
        
        return f"Student(name='{self.name}', age={self.age}, grade={self.grade})"
    
    def __repr__(self):
        
        return f"Student('{self.name}', {self.age}, {self.grade})"

def demonstrate_students():
    
    students = [
        Student("Олександр", 20, 95),
        Student("Марія", 19, 88),
        Student("Іван", 21, 92),
        Student("Анна", 20, 85),
        Student("Петро", 22, 90)
    ]
    
    print("Початковий список студентів:")
    for student in students:
        print(student)
    
    
    sorted_by_name = sorted(students, key=lambda s: s.name)
    print("\nСортування за іменем:")
    for student in sorted_by_name:
        print(student)
    
    
    sorted_by_age = sorted(students, key=lambda s: s.age)
    print("\nСортування за віком:")
    for student in sorted_by_age:
        print(student)
    
    
    sorted_by_grade = sorted(students, key=lambda s: s.grade, reverse=True)
    print("\nСортування за оцінкою (за спаданням):")
    for student in sorted_by_grade:
        print(student)

if __name__ == "__main__":
    demonstrate_students()