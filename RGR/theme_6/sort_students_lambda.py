def sort_students():
    
    students = [
        {'name': 'Олександр', 'grade': 95},
        {'name': 'Марія', 'grade': 88},
        {'name': 'Іван', 'grade': 92},
        {'name': 'Анна', 'grade': 85},
        {'name': 'Петро', 'grade': 90}
    ]
    
    print("Початковий список студентів:")
    for student in students:
        print(f"{student['name']}: {student['grade']}")
    
    
    sorted_by_name = sorted(students, key=lambda x: x['name'])
    print("\nСортування за іменем:")
    for student in sorted_by_name:
        print(f"{student['name']}: {student['grade']}")
    
    
    sorted_by_grade_desc = sorted(students, key=lambda x: x['grade'], reverse=True)
    print("\nСортування за оцінкою (за спаданням):")
    for student in sorted_by_grade_desc:
        print(f"{student['name']}: {student['grade']}")
    
    
    sorted_by_grade_asc = sorted(students, key=lambda x: x['grade'])
    print("\nСортування за оцінкою (за зростанням):")
    for student in sorted_by_grade_asc:
        print(f"{student['name']}: {student['grade']}")

if __name__ == "__main__":
    sort_students()