def prefix_sum(arr):
    prefix = [0] * len(arr)
    prefix[0] = arr[0]

    for i in range(1, len(arr)):
        prefix[i] = prefix[i-1] + arr[i]

    return prefix


arr = [1, 2, 3, 4, 5]
prefix = prefix_sum(arr)

print("Array:", arr)
print("Prefix Sum:", prefix)


# RANGE SUM (L to R)
L = 1
R = 3

if L == 0:
    result = prefix[R]
else:
    result = prefix[R] - prefix[L-1]

print("Sum from index", L, "to", R, ":", result)
