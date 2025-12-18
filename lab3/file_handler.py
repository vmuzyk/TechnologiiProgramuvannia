import csv
from student import Student

class FileHandler:
    
    
    @staticmethod
    def load_from_csv(filename, student_list):
        
        try:
            with open(filename, 'r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                student_list.clear()
                
                for row in reader:
                    student = Student(
                        row["name"],
                        row["phone"],
                        row["email"],
                        row["group"]
                    )
                    student_list.add_student(student)
                
                print(f"Data loaded from {filename}. Total students: {len(student_list)}")
                return True
        except FileNotFoundError:
            print(f"Error: File {filename} not found. Starting with empty list.")
            return False
        except Exception as e:
            print(f"Error loading file: {e}")
            return False
    
    @staticmethod
    def save_to_csv(filename, student_list):
        
        try:
            with open(filename, 'w', newline='', encoding='utf-8') as file:
                fieldnames = ["name", "phone", "email", "group"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                
                for student in student_list:
                    writer.writerow(student.to_dict())
                
                print(f"Data saved to {filename}. Total students: {len(student_list)}")
                return True
        except Exception as e:
            print(f"Error saving file: {e}")
            return False