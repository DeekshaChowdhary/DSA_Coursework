# ---------------------- STUDENT PROFILE CLI ----------------------

"""
Features:
- Add Student
- View Student
- Update Student
- Delete Student
- Exit Program

 Note:
- This version stores only ONE student at a time
"""


# ---------------------- INITIAL DATA ----------------------

student_id = ""
name = ""
age = ""
course = ""


# ---------------------- MAIN LOOP ----------------------

while True:
    print("\n---------- Student Profile Menu ----------")
    print("1. Add Student")
    print("2. View Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")


    # 🔹 ADD STUDENT
    if choice == "1":
        student_id = input("Enter Student ID: ")
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        course = input("Enter Course: ")

        print("Student added successfully")


    # 🔹 VIEW STUDENT
    elif choice == "2":
        if student_id == "":
            print("No student found")
        else:
            print("\n----- Student Details -----")
            print("ID    :", student_id)
            print("Name  :", name)
            print("Age   :", age)
            print("Course:", course)


    # 🔹 UPDATE STUDENT
    elif choice == "3":
        if student_id == "":
            print("No student found to update")
        else:
            name = input("Enter New Name: ")
            age = input("Enter New Age: ")
            course = input("Enter New Course: ")

            print("Student updated successfully")


    # 🔹 DELETE STUDENT
    elif choice == "4":
        if student_id == "":
            print("No student found to delete")
        else:
            student_id = ""
            name = ""
            age = ""
            course = ""

            print("Student deleted successfully")


    # 🔹 EXIT
    elif choice == "5":
        print("Program exited")
        break


    # 🔹 INVALID CHOICE
    else:
        print("Invalid choice, please try again")
