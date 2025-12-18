import csv
import sys
from sys import argv


students_list = []

def load_from_csv(filename):
    
    global students_list
    try:
        with open(filename, 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            students_list = []
            for row in reader:
                students_list.append({
                    "name": row["name"],
                    "phone": row["phone"],
                    "email": row["email"],
                    "group": row["group"]
                })
            
            students_list.sort(key=lambda x: x["name"])
            print(f"Data loaded from {filename}. Total students: {len(students_list)}")
    except FileNotFoundError:
        print(f"Error: File {filename} not found. Starting with empty list.")
    except Exception as e:
        print(f"Error loading file: {e}")

def save_to_csv(filename):
    
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            fieldnames = ["name", "phone", "email", "group"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for student in students_list:
                writer.writerow(student)
        print(f"Data saved to {filename}. Total students: {len(students_list)}")
    except Exception as e:
        print(f"Error saving file: {e}")

def printAllList():
    print("\n--- Student List ---")
    if not students_list:
        print("No students in the list")
    else:
        for elem in students_list:
            strForPrint = f"Student: {elem['name']}, Phone: {elem['phone']}, Email: {elem['email']}, Group: {elem['group']}"
            print(strForPrint)
    print("-------------------\n")
    return len(students_list)

def addNewElement():
    name = input("Please enter student name: ")
    phone = input("Please enter student phone: ")
    email = input("Please enter student email: ")
    group = input("Please enter student group: ")
    
    newItem = {"name": name, "phone": phone, "email": email, "group": group}
    
    
    insertPosition = 0
    for item in students_list:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    students_list.insert(insertPosition, newItem)
    print("New element has been added")
    return newItem

def deleteElement():
    name = input("Please enter name to be deleted: ")
    deletePosition = -1
    for i, item in enumerate(students_list):
        if name == item["name"]:
            deletePosition = i
            break
    if deletePosition == -1:
        print("Element was not found")
        return None
    else:
        deleted_student = students_list[deletePosition]
        print(f"Delete position {deletePosition}")
        del students_list[deletePosition]
        print("Element has been deleted")
        return deleted_student

def updateElement():
    name = input("Please enter name to be updated: ")
    
    
    updatePosition = -1
    for i, item in enumerate(students_list):
        if name == item["name"]:
            updatePosition = i
            break
    
    if updatePosition == -1:
        print("Student not found")
        return None
    
    
    oldStudent = students_list[updatePosition]
    
    print(f"Current data: Name: {oldStudent['name']}, Phone: {oldStudent['phone']}, Email: {oldStudent['email']}, Group: {oldStudent['group']}")
    
    
    new_name = input(f"Enter new name (current: {oldStudent['name']}): ").strip()
    new_phone = input(f"Enter new phone (current: {oldStudent['phone']}): ").strip()
    new_email = input(f"Enter new email (current: {oldStudent['email']}): ").strip()
    new_group = input(f"Enter new group (current: {oldStudent['group']}): ").strip()
    
    
    if not new_name:
        new_name = oldStudent['name']
    if not new_phone:
        new_phone = oldStudent['phone']
    if not new_email:
        new_email = oldStudent['email']
    if not new_group:
        new_group = oldStudent['group']
    
    
    del students_list[updatePosition]
    
    
    updatedItem = {"name": new_name, "phone": new_phone, "email": new_email, "group": new_group}
    
    
    insertPosition = 0
    for item in students_list:
        if new_name > item["name"]:
            insertPosition += 1
        else:
            break
    
    
    students_list.insert(insertPosition, updatedItem)
    print("Element has been updated")
    return updatedItem

def main():
    
    if len(argv) < 2:
        print("Usage: python phonebook.py <csv_filename>")
        print("Starting with empty student list...")
    else:
        csv_filename = argv[1]
        load_from_csv(csv_filename)
    
    print("Student Directory Management System")
    print("Current list:")
    printAllList()
    
    while True:
        choice = input("Please specify the action [ C create, U update, D delete, P print, S save, X exit ] ")
        match choice:
            case "C" | "c":
                print("New element will be created:")
                addNewElement()
                printAllList()
            case "U" | "u":
                print("Existing element will be updated")
                updateElement()
                printAllList()
            case "D" | "d":
                print("Element will be deleted")
                deleteElement()
                printAllList()
            case "P" | "p":
                print("List will be printed")
                printAllList()
            case "S" | "s":
                if len(argv) >= 2:
                    save_to_csv(argv[1])
                else:
                    filename = input("Enter filename to save: ")
                    save_to_csv(filename)
            case "X" | "x":
                
                if len(argv) >= 2:
                    save_to_csv(argv[1])
                else:
                    save_choice = input("Save before exit? (y/n): ")
                    if save_choice.lower() == 'y':
                        filename = input("Enter filename to save: ")
                        save_to_csv(filename)
                print("Exit()")
                break
            case _:
                print("Wrong choice")

if __name__ == "__main__":
    main()