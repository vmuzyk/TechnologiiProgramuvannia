from student import Student

class StudentList:
    
    
    def __init__(self):
        self.students = []
    
    def add_student(self, student):
        
        insert_position = 0
        for existing_student in self.students:
            if student.name > existing_student.name:
                insert_position += 1
            else:
                break
        self.students.insert(insert_position, student)
        return student
    
    def delete_student(self, name):
        
        for i, student in enumerate(self.students):
            if student.name == name:
                deleted_student = self.students[i]
                del self.students[i]
                return deleted_student
        return None
    
    def update_student(self, old_name, new_student_data):
        
        
        deleted_student = self.delete_student(old_name)
        if not deleted_student:
            return None
        
        
        updated_student = Student(
            new_student_data.get('name', deleted_student.name),
            new_student_data.get('phone', deleted_student.phone),
            new_student_data.get('email', deleted_student.email),
            new_student_data.get('group', deleted_student.group)
        )
        
      
        return self.add_student(updated_student)
    
    def find_student(self, name):
        
        for student in self.students:
            if student.name == name:
                return student
        return None
    
    def get_all_students(self):
        
        return self.students.copy()
    
    def print_all(self):
        
        print("\n--- Student List ---")
        if not self.students:
            print("No students in the list")
        else:
            for student in self.students:
                print(student)
        print("-------------------\n")
        return len(self.students)
    
    def clear(self):
        
        self.students.clear()
    
    def __len__(self):
        return len(self.students)
    
    def __iter__(self):
        return iter(self.students)