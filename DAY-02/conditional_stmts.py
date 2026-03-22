
#------PYTHON CONDITIONAL STATEMENTS-------------


"""
 Topics Covered:
1. if
2. if-else
3. if-elif-else
4. nested if
5. logical operators (and, or)
6. membership (in)
7. not operator
"""


#  1. IF → runs only when condition is TRUE
balance = 2000
if balance > 1000:
    print("You have money")


#  2. IF-ELSE → one block will run
age = 18
if age >= 18:
    print("Adult")
else:
    print("Child")


#  3. IF-ELIF-ELSE → multiple conditions
marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")


#  4. NESTED IF → if inside another if
is_logged = True
is_premium = True

if is_logged:
    if is_premium:
        print("Premium User")
    else:
        print("Free User")
else:
    print("Please Login")


#  5. LOGICAL OPERATORS (and, or)
age = 25
income = 50000

if age >= 18 and income >= 30000:
    print("Eligible for loan")


#  6. MEMBERSHIP (in)
fruits = ["apple", "mango", "banana"]

if "orange" in fruits:
    print("Orange found")
else:
    print("Orange not found")


#  7. NOT operator (reverse condition)
is_raining = False

if not is_raining:
    print("Go outside")


