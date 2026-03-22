#------- TIME COMPLEXITY ------------


"""
Time Complexity tells how fast or slow a program runs based on input size (n).
"""


# O(1) - CONSTANT TIME
# Same time no matter input size

array = [1, 2, 3, 4, 5]

print("Array:", array)
print("Access element:", array[3])   # Direct access
print("Time Complexity: O(1)")

# Accessing any index takes SAME time
# Doesn't matter if array has 5 or 1000 elements



# O(n) - LINEAR TIME
# Time increases as input increases

array = [1, 2, 3, 4, 5]

print("\nLinear loop:")
for i in array:
    print(i)
print("Time Complexity: O(n)")

# Loop runs 'n' times (for each element)


# O(n^2) - QUADRATIC TIME
# Nested loops → slower

n = 4
print("\nNested loop:")
for i in range(n):
    for j in range(n):
        print(i, j)
print("Time Complexity: O(n^2)")

# Outer loop runs n times
# Inner loop runs n times
# Total = n × n = n²
