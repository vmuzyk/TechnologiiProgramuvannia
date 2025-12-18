import pytest
import csv
import os
import tempfile
import sys
from io import StringIO


from student import Student
from student_list import StudentList
from file_handler import FileHandler

def test_student_creation():
    
    student = Student("Test Student", "0639999999", "test@example.com", "TP-KB-22-1")
    assert student.name == "Test Student"
    assert student.phone == "0639999999"
    assert student.email == "test@example.com"
    assert student.group == "TP-KB-22-1"

def test_student_to_dict():
    
    student = Student("Test Student", "0639999999", "test@example.com", "TP-KB-22-1")
    student_dict = student.to_dict()
    assert student_dict == {
        'name': 'Test Student',
        'phone': '0639999999',
        'email': 'test@example.com',
        'group': 'TP-KB-22-1'
    }

def test_student_from_dict():
    
    data = {
        'name': 'Test Student',
        'phone': '0639999999',
        'email': 'test@example.com',
        'group': 'TP-KB-22-1'
    }
    student = Student.from_dict(data)
    assert student.name == "Test Student"
    assert student.phone == "0639999999"

def test_student_list_add():
    
    student_list = StudentList()
    student1 = Student("Alice", "0631111111", "alice@example.com", "TP-KB-22-1")
    student2 = Student("Bob", "0632222222", "bob@example.com", "TP-KB-22-1")
    
    student_list.add_student(student1)
    student_list.add_student(student2)
    
    assert len(student_list) == 2
    assert student_list.students[0].name == "Alice"
    assert student_list.students[1].name == "Bob"

def test_student_list_sorted_insertion():
    
    student_list = StudentList()
    student1 = Student("Charlie", "0633333333", "charlie@example.com", "TP-KB-22-1")
    student2 = Student("Alice", "0631111111", "alice@example.com", "TP-KB-22-1")
    student3 = Student("Bob", "0632222222", "bob@example.com", "TP-KB-22-1")
    
    student_list.add_student(student1)
    student_list.add_student(student2)
    student_list.add_student(student3)
    
    assert len(student_list) == 3
    assert student_list.students[0].name == "Alice"
    assert student_list.students[1].name == "Bob"
    assert student_list.students[2].name == "Charlie"

def test_student_list_delete():
    
    student_list = StudentList()
    student = Student("Test Student", "0639999999", "test@example.com", "TP-KB-22-1")
    student_list.add_student(student)
    
    deleted = student_list.delete_student("Test Student")
    assert deleted is not None
    assert deleted.name == "Test Student"
    assert len(student_list) == 0

def test_student_list_delete_not_found():
    
    student_list = StudentList()
    student = Student("Existing Student", "0635555555", "existing@example.com", "TP-KB-22-1")
    student_list.add_student(student)
    
    deleted = student_list.delete_student("Non Existent")
    assert deleted is None
    assert len(student_list) == 1

def test_student_list_update():
    
    student_list = StudentList()
    student = Student("Old Name", "0634444444", "old@example.com", "TP-KB-22-1")
    student_list.add_student(student)
    
    new_data = {
        'name': 'New Name',
        'phone': '0631111111',
        'email': 'new@example.com',
        'group': 'TP-KB-22-2'
    }
    
    updated = student_list.update_student("Old Name", new_data)
    assert updated is not None
    assert updated.name == "New Name"
    assert updated.phone == "0631111111"
    assert len(student_list) == 1

def test_file_handler_save_load():
    
    student_list = StudentList()
    student1 = Student("Alice", "0631111111", "alice@example.com", "TP-KB-22-1")
    student2 = Student("Bob", "0632222222", "bob@example.com", "TP-KB-22-1")
    student_list.add_student(student1)
    student_list.add_student(student2)
    
    
    with tempfile.NamedTemporaryFile(mode='r', suffix='.csv', delete=False) as f:
        temp_filename = f.name
    
    try:
        
        result = FileHandler.save_to_csv(temp_filename, student_list)
        assert result == True
        assert os.path.exists(temp_filename)
        
        
        new_student_list = StudentList()
        result = FileHandler.load_from_csv(temp_filename, new_student_list)
        assert result == True
        assert len(new_student_list) == 2
        assert new_student_list.students[0].name == "Alice"
        assert new_student_list.students[1].name == "Bob"
        
    finally:
        if os.path.exists(temp_filename):
            os.unlink(temp_filename)

def test_student_str_representation():
    
    student = Student("Test Student", "0639999999", "test@example.com", "TP-KB-22-1")
    expected_str = "Student: Test Student, Phone: 0639999999, Email: test@example.com, Group: TP-KB-22-1"
    assert str(student) == expected_str

def test_student_list_print_all(capsys):
    
    student_list = StudentList()
    student1 = Student("Print Test 1", "0632222222", "print1@example.com", "TP-KB-22-1")
    student2 = Student("Print Test 2", "0633333333", "print2@example.com", "TP-KB-22-1")
    student_list.add_student(student1)
    student_list.add_student(student2)
    
    count = student_list.print_all()
    assert count == 2
    
    captured = capsys.readouterr()
    assert "Print Test 1" in captured.out
    assert "Print Test 2" in captured.out

if __name__ == "__main__":
    pytest.main([__file__])