from student import Student

class StudentList:
    """Клас для роботи зі списком студентів"""
    
    def __init__(self):
        self.students = []
    
    def add_student(self, student):
        """Додає студента до списку зі збереженням сортування"""
        insert_position = 0
        for existing_student in self.students:
            if student.name > existing_student.name:
                insert_position += 1
            else:
                break
        self.students.insert(insert_position, student)
        return student
    
    def delete_student(self, name):
        """Видаляє студента за іменем"""
        for i, student in enumerate(self.students):
            if student.name == name:
                deleted_student = self.students[i]
                del self.students[i]
                return deleted_student
        return None
    
    def update_student(self, old_name, new_student_data):
        """Оновлює дані студента"""
        # Видаляємо старого студента
        deleted_student = self.delete_student(old_name)
        if not deleted_student:
            return None
        
        # Створюємо оновленого студента
        updated_student = Student(
            new_student_data.get('name', deleted_student.name),
            new_student_data.get('phone', deleted_student.phone),
            new_student_data.get('email', deleted_student.email),
            new_student_data.get('group', deleted_student.group)
        )
        
        # Додаємо оновленого студента
        return self.add_student(updated_student)
    
    def find_student(self, name):
        """Знаходить студента за іменем"""
        for student in self.students:
            if student.name == name:
                return student
        return None
    
    def get_all_students(self):
        """Повертає список всіх студентів"""
        return self.students.copy()
    
    def print_all(self):
        """Виводить список всіх студентів"""
        print("\n--- Student List ---")
        if not self.students:
            print("No students in the list")
        else:
            for student in self.students:
                print(student)
        print("-------------------\n")
        return len(self.students)
    
    def clear(self):
        """Очищає список студентів"""
        self.students.clear()
    
    def __len__(self):
        return len(self.students)
    
    def __iter__(self):
        return iter(self.students)