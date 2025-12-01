import json
import os

MONTHS = ["June", "July", "August", "September", "October", "November", 
          "December", "January", "February", "March", "April", "May"]
DATABASE_FILE = 'data.json'

def load_data():
    if os.path.exists(DATABASE_FILE):
        try:
            with open(DATABASE_FILE, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Error reading database. Starting fresh.")
            return initialize_data()
    else:
        return initialize_data()

def initialize_data():
    return {"classes": {}}

def save_data(data):
    with open(DATABASE_FILE, 'w') as file:
        json.dump(data, file, indent=4)
    print("✓ Data saved successfully.")

def add_class(data):
    class_name = input("Enter class name (e.g., 10-A, Class IX): ").strip()
    
    if class_name in data["classes"]:
        print(f"✗ Class '{class_name}' already exists.")
        return
    
    try:
        monthly_fee = int(input("Enter monthly fee for this class: "))
        if monthly_fee <= 0:
            print("✗ Fee must be positive.")
            return
    except ValueError:
        print("✗ Invalid fee amount.")
        return
    
    data["classes"][class_name] = {
        "monthly_fee": monthly_fee,
        "students": {}
    }
    save_data(data)
    print(f"✓ Class '{class_name}' created successfully.")

def add_student(data):
    if not data["classes"]:
        print("✗ No classes available. Please create a class first.")
        return
    
    print("\nAvailable Classes:")
    for i, class_name in enumerate(data["classes"].keys(), 1):
        print(f"{i}. {class_name}")
    
    try:
        class_choice = int(input("Select class number: ")) - 1
        class_list = list(data["classes"].keys())
        if class_choice < 0 or class_choice >= len(class_list):
            print("✗ Invalid class selection.")
            return
        
        selected_class = class_list[class_choice]
    except ValueError:
        print("✗ Invalid input.")
        return
    
    student_name = input("Enter student name: ").strip()
    student_roll = input("Enter student roll number: ").strip()
    
    if student_roll in data["classes"][selected_class]["students"]:
        print(f"✗ Student with roll number '{student_roll}' already exists in this class.")
        return
    
    data["classes"][selected_class]["students"][student_roll] = {
        "name": student_name,
        "monthly_fee": data["classes"][selected_class]["monthly_fee"],
        "total_paid": 0,
        "total_due": data["classes"][selected_class]["monthly_fee"] * 10,
        "payments": {}
    }
    
    save_data(data)
    print(f"✓ Student '{student_name}' (Roll No: {student_roll}) added to class '{selected_class}'.")

def record_payment(data):
    if not data["classes"]:
        print("✗ No classes available.")
        return
    
    print("\nAvailable Classes:")
    for i, class_name in enumerate(data["classes"].keys(), 1):
        print(f"{i}. {class_name}")
    
    try:
        class_choice = int(input("Select class number: ")) - 1
        class_list = list(data["classes"].keys())
        if class_choice < 0 or class_choice >= len(class_list):
            print("✗ Invalid class selection.")
            return
        
        selected_class = class_list[class_choice]
        class_data = data["classes"][selected_class]
        
        if not class_data["students"]:
            print("✗ No students in this class.")
            return
        
        print("\nStudents in this class:")
        for i, (roll, student) in enumerate(class_data["students"].items(), 1):
            print(f"{i}. {student['name']} (Roll No: {roll})")
        
        student_choice = int(input("Select student number: ")) - 1
        student_list = list(class_data["students"].items())
        if student_choice < 0 or student_choice >= len(student_list):
            print("✗ Invalid student selection.")
            return
        
        roll, student = student_list[student_choice]
        
        print(f"\nRecording payment for {student['name']}")
        print(f"Monthly fee: ₹{student['monthly_fee']}")
        
        month = input("Enter month (e.g., january, february): ").strip().capitalize()
        if month not in MONTHS:
            print(f"✗ Invalid month. Choose from: {', '.join(MONTHS)}")
            return
        
        try:
            amount = int(input("Enter amount to pay: "))
            if amount <= 0:
                print("✗ Amount must be positive.")
                return
            if amount > student['monthly_fee']:
                print(f"✗ Cannot exceed monthly fee of ₹{student['monthly_fee']}")
                return
        except ValueError:
            print("✗ Invalid amount.")
            return
        
        if month in student['payments']:
            print(f"✗ Payment already recorded for {month}. Current payment: ₹{student['payments'][month]}")
            return
        
        student['payments'][month] = amount
        student['total_paid'] += amount
        student['total_due'] = (student['monthly_fee'] * 10) - student['total_paid']
        
        save_data(data)
        print(f"✓ Payment of ₹{amount} recorded for {month}.")
    except ValueError:
        print("✗ Invalid input.")

def view_student_details(data):
    if not data["classes"]:
        print("✗ No classes available.")
        return
    
    print("\nAvailable Classes:")
    for i, class_name in enumerate(data["classes"].keys(), 1):
        print(f"{i}. {class_name}")
    
    try:
        class_choice = int(input("Select class number: ")) - 1
        class_list = list(data["classes"].keys())
        if class_choice < 0 or class_choice >= len(class_list):
            print("✗ Invalid class selection.")
            return
        
        selected_class = class_list[class_choice]
        class_data = data["classes"][selected_class]
        
        if not class_data["students"]:
            print("✗ No students in this class.")
            return
        
        print("\nStudents in this class:")
        for i, (roll, student) in enumerate(class_data["students"].items(), 1):
            print(f"{i}. {student['name']} (Roll No: {roll})")
        
        student_choice = int(input("Select student number: ")) - 1
        student_list = list(class_data["students"].items())
        if student_choice < 0 or student_choice >= len(student_list):
            print("✗ Invalid student selection.")
            return
        
        roll, student = student_list[student_choice]
        
        print(f"\n{'='*50}")
        print(f"Student: {student['name']} | Roll No: {roll} | Class: {selected_class}")
        print(f"{'='*50}")
        print(f"Monthly Fee: ₹{student['monthly_fee']}")
        print(f"Total Paid: ₹{student['total_paid']}")
        print(f"Total Due: ₹{student['total_due']}")
        print(f"\n--- Payment Status ---")
        
        for month in MONTHS:
            if month in student['payments']:
                print(f"{month}: ✓ Paid ₹{student['payments'][month]}")
            else:
                print(f"{month}: ✗ Not Paid")
        
        print(f"{'='*50}")
    except ValueError:
        print("✗ Invalid input.")

def view_class_report(data):
    if not data["classes"]:
        print("✗ No classes available.")
        return
    
    print("\nAvailable Classes:")
    for i, class_name in enumerate(data["classes"].keys(), 1):
        print(f"{i}. {class_name}")
    
    try:
        class_choice = int(input("Select class number: ")) - 1
        class_list = list(data["classes"].keys())
        if class_choice < 0 or class_choice >= len(class_list):
            print("✗ Invalid class selection.")
            return
        
        selected_class = class_list[class_choice]
        class_data = data["classes"][selected_class]
        
        print(f"\n{'='*70}")
        print(f"Class: {selected_class} | Monthly Fee: ₹{class_data['monthly_fee']}")
        print(f"{'='*70}")
        
        if not class_data["students"]:
            print("✗ No students in this class.")
            return
        
        total_due = 0
        total_paid = 0
        
        for roll, student in class_data["students"].items():
            print(f"\n{student['name']} (Roll No: {roll})")
            print(f"  Paid: ₹{student['total_paid']} | Due: ₹{student['total_due']}")
            total_paid += student['total_paid']
            total_due += student['total_due']
        
        print(f"\n{'='*70}")
        print(f"Class Total - Paid: ₹{total_paid} | Due: ₹{total_due}")
        print(f"{'='*70}")
    except ValueError:
        print("✗ Invalid input.")

def main_menu():
    while True:
        print("\n" + "="*50)
        print("SCHOOL FEE MANAGEMENT SYSTEM")
        print("="*50)
        print("1. Add New Class")
        print("2. Add Student to Class")
        print("3. Record Fee Payment")
        print("4. View Student Details")
        print("5. View Class Report")
        print("6. Exit")
        print("="*50)
        
        try:
            choice = int(input("Select an option (1-6): "))
            
            if choice == 1:
                add_class(data)
            elif choice == 2:
                add_student(data)
            elif choice == 3:
                record_payment(data)
            elif choice == 4:
                view_student_details(data)
            elif choice == 5:
                view_class_report(data)
            elif choice == 6:
                print("\nThank you for using School Fee Management System!")
                break
            else:
                print("✗ Invalid choice. Please select 1-6.")
        except ValueError:
            print("✗ Invalid input. Please enter a number.")
        except KeyboardInterrupt:
            print("\n\nExiting...")
            break
        except Exception as e:
            print(f"✗ An error occurred: {e}")

if __name__ == "__main__":
    data = load_data()
    main_menu()
