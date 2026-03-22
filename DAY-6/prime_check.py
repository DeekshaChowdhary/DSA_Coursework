# ------------------ AREA FUNCTION ------------------
def cal_area(length, breadth):
    return length * breadth

print("Area:", cal_area(5, 6))


# ------------------ PRIME CHECK ------------------
def is_prime(num):
    if num <= 1:
        return False
    
    for i in range(2, num):
        if num % i == 0:
            return False   # divisible → not prime
    
    return True            # no divisors → prime


# ------------------ MAIN ------------------
num = int(input("\nEnter number: "))

if is_prime(num):
    print("Prime number")
else:
    print("Not prime (Composite)")
