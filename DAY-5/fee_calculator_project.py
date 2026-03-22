# ---------------------- FEE CALCULATOR ----------------------

"""
Features:
- Select course
- Apply discount based on marks
- Handle invalid input

This project will introduce conditional logic in real time project.

"""


# ---------------------- FUNCTION ----------------------

def calculate_fee(course, marks):
    """Calculate final fee based on course and marks"""

    # Course selection
    if course == "AI":
        fee = 50000
    elif course == "Web":
        fee = 30000
    elif course == "Data Science":
        fee = 40000
    else:
        return None   # Invalid course

    # Discount condition
    if marks > 90:
        fee -= 5000

    return fee


# ---------------------- MAIN PROGRAM ----------------------

def main():
    course = input("Enter course (AI / Web / Data Science): ")
    marks = int(input("Enter marks: "))

    fee = calculate_fee(course, marks)

    if fee is None:
        print("Invalid course selected")
    else:
        print("Final fee:", fee)


# ---------------------- RUN ----------------------

if __name__ == "__main__":
    main()
