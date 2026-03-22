#------------LOOPS IN PYTHON----------------------- 

#  1. PRINT 1 TO 5

print("Numbers from 1 to 5 (FOR loop):")
for i in range(1, 6):
    print(i)

print("Numbers from 1 to 5 (WHILE loop):")
i = 1
while i <= 5:
    print(i)
    i += 1


#  2. PRINT 1 TO N

n = int(input("Enter a number: "))

print("Using FOR loop:")
for i in range(1, n + 1):
    print(i)

print("Using WHILE loop:")
i = 1
while i <= n:
    print(i)
    i += 1


#  3. EVEN NUMBERS

print("Even numbers:")
for i in range(2, n + 1, 2):
    print(i)


# 4. ODD NUMBERS

print("Odd numbers:")
for i in range(1, n + 1, 2):
    print(i)


#  5. SUM OF NUMBERS (1 to N)

total = 0
for i in range(1, n + 1):
    total += i

print("Sum of numbers:", total)


#  6. SUM OF EVEN NUMBERS

even_sum = 0
for i in range(2, n * 2 + 1, 2):
    even_sum += i

print("Sum of first", n, "even numbers:", even_sum)


