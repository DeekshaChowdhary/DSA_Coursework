#----------- NUMBER PROGRAMS IN PYTHON--------------------------

import math

#  1. EVEN OR ODD
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")


#  2. BIGGEST & SMALLEST (3 numbers)
a = int(input("\nEnter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

print("Biggest:", max(a, b, c))
print("Smallest:", min(a, b, c))


#  3. PRIME NUMBER
num = int(input("\nEnter number to check prime: "))

if num < 2:
    print("Not Prime")
else:
    prime = True
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            prime = False
            break

    if prime:
        print("Prime Number")
    else:
        print("Not Prime")


#  4. POSITIVE / NEGATIVE / ZERO
num = int(input("\nEnter number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


#  5. ARMSTRONG NUMBER
num = int(input("\nEnter number: "))

temp = num
power = len(str(num))
total = 0

while temp > 0:
    digit = temp % 10
    total += digit ** power
    temp //= 10

if total == num:
    print("Armstrong Number")
else:
    print("Not Armstrong")


#  6. PERFECT NUMBER
num = int(input("\nEnter number: "))

sum_div = 0
for i in range(1, num):
    if num % i == 0:
        sum_div += i

if sum_div == num:
    print("Perfect Number")
else:
    print("Not Perfect")


#  7. SUM OF N NUMBERS
n = int(input("\nEnter n: "))
total = 0
for i in range(1, n + 1):
    total += i
print("Sum:", total)


#  8. SUM OF EVEN NUMBERS
even_sum = 0
for i in range(2, n * 2 + 1, 2):
    even_sum += i
print("Even Sum:", even_sum)
