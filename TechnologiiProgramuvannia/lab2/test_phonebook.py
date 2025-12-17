import pytest
import csv
import os
import tempfile
import sys
from io import StringIO

# Імпортуємо всі функції, але НЕ глобальну змінну
from phonebook import load_from_csv, save_to_csv, printAllList, addNewElement, deleteElement, updateElement

def test_load_from_csv():
    """Test loading students from CSV file"""
    # Create a temporary CSV file for testing
    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
        writer = csv.DictWriter(f, fieldnames=['name', 'phone', 'email', 'group'])
        writer.writeheader()
        writer.writerow({'name': 'Test Student', 'phone': '0639999999', 'email': 'test@example.com', 'group': 'TP-KB-22-1'})
        temp_filename = f.name
    
    try:
        # Import the module to access students_list
        import phonebook
        
        # Test loading
        load_from_csv(temp_filename)
        assert len(phonebook.students_list) == 1
        assert phonebook.students_list[0]['name'] == 'Test Student'
        assert phonebook.students_list[0]['phone'] == '0639999999'
        
        # Clean up for next test
        phonebook.students_list.clear()
    finally:
        os.unlink(temp_filename)

def test_save_to_csv():
    """Test saving students to CSV file"""
    import phonebook
    
    # Add test data
    phonebook.students_list.append({'name': 'Save Test', 'phone': '0638888888', 'email': 'save@example.com', 'group': 'TP-KB-22-1'})
    
    # Save to temporary file
    with tempfile.NamedTemporaryFile(mode='r', suffix='.csv', delete=False) as f:
        temp_filename = f.name
    
    try:
        save_to_csv(temp_filename)
        
        # Verify the file was created and contains correct data
        assert os.path.exists(temp_filename)
        
        with open(temp_filename, 'r') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
            assert len(rows) == 1
            assert rows[0]['name'] == 'Save Test'
            assert rows[0]['phone'] == '0638888888'
            
        # Clean up
        phonebook.students_list.clear()
    finally:
        if os.path.exists(temp_filename):
            os.unlink(temp_filename)

def test_add_new_element(monkeypatch):
    """Test adding a new student"""
    import phonebook
    
    # Mock user input
    inputs = iter(["Test Add", "0637777777", "add@example.com", "TP-KB-22-1"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    result = addNewElement()
    assert len(phonebook.students_list) == 1
    assert phonebook.students_list[0]['name'] == 'Test Add'
    assert result['name'] == 'Test Add'
    
    # Clean up
    phonebook.students_list.clear()

def test_delete_element(monkeypatch):
    """Test deleting a student"""
    import phonebook
    phonebook.students_list.append({'name': 'Delete Test', 'phone': '0636666666', 'email': 'delete@example.com', 'group': 'TP-KB-22-1'})
    
    # Mock user input
    monkeypatch.setattr('builtins.input', lambda _: "Delete Test")
    
    result = deleteElement()
    assert len(phonebook.students_list) == 0
    assert result['name'] == 'Delete Test'

def test_delete_element_not_found(monkeypatch):
    """Test deleting a non-existent student"""
    import phonebook
    phonebook.students_list.append({'name': 'Existing Student', 'phone': '0635555555', 'email': 'existing@example.com', 'group': 'TP-KB-22-1'})
    
    # Mock user input
    monkeypatch.setattr('builtins.input', lambda _: "Non Existent")
    
    initial_count = len(phonebook.students_list)
    result = deleteElement()
    assert len(phonebook.students_list) == initial_count
    assert result is None
    
    phonebook.students_list.clear()

def test_update_element(monkeypatch):
    """Test updating a student"""
    import phonebook
    phonebook.students_list.append({'name': 'Update Test', 'phone': '0634444444', 'email': 'update@example.com', 'group': 'TP-KB-22-1'})
    
    # Mock user input
    inputs = iter(["Update Test", "Updated Name", "0631111111", "updated@example.com", "TP-KB-22-2"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    result = updateElement()
    assert len(phonebook.students_list) == 1
    assert phonebook.students_list[0]['name'] == 'Updated Name'
    assert result['name'] == 'Updated Name'
    
    phonebook.students_list.clear()

def test_print_all_list(capsys):
    """Test printing all students"""
    import phonebook
    phonebook.students_list.extend([
        {'name': 'Print Test 1', 'phone': '0632222222', 'email': 'print1@example.com', 'group': 'TP-KB-22-1'},
        {'name': 'Print Test 2', 'phone': '0633333333', 'email': 'print2@example.com', 'group': 'TP-KB-22-1'}
    ])
    
    count = printAllList()
    assert count == 2
    
    # Capture printed output
    captured = capsys.readouterr()
    assert "Print Test 1" in captured.out
    assert "Print Test 2" in captured.out
    
    phonebook.students_list.clear()

def test_print_empty_list(capsys):
    """Test printing empty list"""
    import phonebook
    
    count = printAllList()
    assert count == 0
    
    # Capture printed output
    captured = capsys.readouterr()
    assert "No students in the list" in captured.out

def test_sorted_insertion(monkeypatch):
    """Test that new elements are inserted in sorted order"""
    import phonebook
    phonebook.students_list.extend([
        {'name': 'Alice', 'phone': '0631111111', 'email': 'alice@example.com', 'group': 'TP-KB-22-1'},
        {'name': 'Charlie', 'phone': '0633333333', 'email': 'charlie@example.com', 'group': 'TP-KB-22-1'}
    ])
    
    # Mock user input for adding "Bob"
    inputs = iter(["Bob", "0632222222", "bob@example.com", "TP-KB-22-1"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    addNewElement()
    assert len(phonebook.students_list) == 3
    assert phonebook.students_list[0]['name'] == 'Alice'
    assert phonebook.students_list[1]['name'] == 'Bob'
    assert phonebook.students_list[2]['name'] == 'Charlie'
    
    phonebook.students_list.clear()