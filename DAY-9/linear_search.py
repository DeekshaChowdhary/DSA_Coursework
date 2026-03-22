#--------LINEAR SEARCH---------------
arr = [50, 20, 40, 30, 10]
target = 30

for i in range(len(arr)):
    if arr[i] == target:
        print("Found at index:", i)
        break
else:
    print("Not found")


# COUNT TARGET
arr = [50, 40, 30, 20, 30, 10, 30]
target = 30
count = 0

for num in arr:
    if num == target:
        count += 1

print("Count:", count)


# FIND FIRST NEGATIVE NUMBER
arr = [50, 30, 20, -2, -3, -4]

for num in arr:
    if num < 0:
        print("First negative:", num)
        break
else:
    print("No negative number")
