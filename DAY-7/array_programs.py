
#------- ARRAY PROGRAMS ---------------


# 🔹 1. SUM OF ELEMENTS
arr = list(map(int, input("Enter numbers: ").split()))

total = 0
for num in arr:
    total += num

print("Sum:", total)


# 🔹 2. COUNT ELEMENTS
count = 0
for i in arr:
    count += 1

print("Count:", count)


# 🔹 3. COUNT EVEN NUMBERS
even_count = 0
for i in arr:
    if i % 2 == 0:
        even_count += 1

print("Even count:", even_count)


# 🔹 4. FIND MAX VALUE
max_val = arr[0]

for i in arr:
    if i > max_val:
        max_val = i

print("Max value:", max_val)
