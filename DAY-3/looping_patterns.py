# ----------------- LOOPING PATTERNS------------------


n = int(input("Enter number of rows: "))


#  1. STAR PATTERN (increasing)
print("\nStar Pattern 1:")
for i in range(1, n+1):
    for j in range(i):
        print("*", end=" ")
    print()


#  2. STAR PATTERN (same using *)
print("\nStar Pattern 2:")
for i in range(1, n+1):
    print("* " * i)


#  3. REVERSE STAR PATTERN
print("\nReverse Star Pattern:")
for i in range(n, 0, -1):
    print("* " * i)


#  4. NUMBER PATTERN (1, 1 2, 1 2 3)
print("\nNumber Pattern:")
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()


#  5. SAME NUMBER PATTERN (1, 2 2, 3 3 3)
print("\nSame Number Pattern:")
for i in range(1, n+1):
    for j in range(i):
        print(i, end=" ")
    print()


#  6. UPSIDE DOWN NUMBER PATTERN
print("\nUpside Down Pattern:")
for i in range(n, 0, -1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()
