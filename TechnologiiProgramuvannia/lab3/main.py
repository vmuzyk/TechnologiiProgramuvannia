import sys
from student import Student
from student_list import StudentList
from file_handler import FileHandler

def add_new_element(student_list):
    """Додає нового студента"""
    name = input("Please enter student name: ")
    phone = input("Please enter student phone: ")
    email = input("Please enter student email: ")
    group = input("Please enter student group: ")
    
    student = Student(name, phone, email, group)
    student_list.add_student(student)
    print("New element has been added")
    return student

def delete_element(student_list):
    """Видаляє студента"""
    name = input("Please enter name to be deleted: ")
    
    deleted_student = student_list.delete_student(name)
    if deleted_student:
        print(f"Student {name} has been deleted")
        return deleted_student
    else:
        print("Element was not found")
        return None

def update_element(student_list):
    """Оновлює дані студента"""
    name = input("Please enter name to be updated: ")
    
    student = student_list.find_student(name)
    if not student:
        print("Student not found")
        return None
    
    print(f"Current data: {student}")
    
    new_name = input(f"Enter new name (current: {student.name}): ").strip()
    new_phone = input(f"Enter new phone (current: {student.phone}): ").strip()
    new_email = input(f"Enter new email (current: {student.email}): ").strip()
    new_group = input(f"Enter new group (current: {student.group}): ").strip()
    
    new_data = {}
    if new_name:
        new_data['name'] = new_name
    if new_phone:
        new_data['phone'] = new_phone
    if new_email:
        new_data['email'] = new_email
    if new_group:
        new_data['group'] = new_group
    
    updated_student = student_list.update_student(name, new_data)
    if updated_student:
        print("Element has been updated")
    return updated_student

def main():
    # Ініціалізація об'єктів
    student_list = StudentList()
    
    # Завантаження даних з командного рядка
    if len(sys.argv) < 2:
        print("Usage: python main.py <csv_filename>")
        print("Starting with empty student list...")
    else:
        csv_filename = sys.argv[1]
        FileHandler.load_from_csv(csv_filename, student_list)
    
    print("Student Directory Management System (OOP Version)")
    student_list.print_all()
    
    while True:
        choice = input("Please specify the action [ C create, U update, D delete, P print, S save, X exit ] ")
        match choice:
            case "C" | "c":
                print("New element will be created:")
                add_new_element(student_list)
                student_list.print_all()
            case "U" | "u":
                print("Existing element will be updated")
                update_element(student_list)
                student_list.print_all()
            case "D" | "d":
                print("Element will be deleted")
                delete_element(student_list)
                student_list.print_all()
            case "P" | "p":
                print("List will be printed")
                student_list.print_all()
            case "S" | "s":
                if len(sys.argv) >= 2:
                    FileHandler.save_to_csv(sys.argv[1], student_list)
                else:
                    filename = input("Enter filename to save: ")
                    FileHandler.save_to_csv(filename, student_list)
            case "X" | "x":
                # Авто-збереження перед виходом
                if len(sys.argv) >= 2:
                    FileHandler.save_to_csv(sys.argv[1], student_list)
                else:
                    save_choice = input("Save before exit? (y/n): ")
                    if save_choice.lower() == 'y':
                        filename = input("Enter filename to save: ")
                        FileHandler.save_to_csv(filename, student_list)
                print("Exit()")
                break
            case _:
                print("Wrong choice")

if __name__ == "__main__":
    main()