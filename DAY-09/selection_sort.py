# SELECTION SORT (ASCENDING)
arr = [63, 25, 12, 22, 11]

for i in range(len(arr)):
    min_index = i

    for j in range(i+1, len(arr)):
        if arr[j] < arr[min_index]:
            min_index = j

    arr[i], arr[min_index] = arr[min_index], arr[i]

print("Ascending:", arr)


# SELECTION SORT (DESCENDING)
arr = [63, 25, 12, 22, 11]

for i in range(len(arr)):
    max_index = i

    for j in range(i+1, len(arr)):
        if arr[j] > arr[max_index]:
            max_index = j

    arr[i], arr[max_index] = arr[max_index], arr[i]

print("Descending:", arr)


#To print an element of an entered index number:
def smallest_index(arr, k):
    arr.sort()
    return arr[k-1]

arr = [63, 25, 12, 22, 11]
k = int(input("Enter position: "))

print(k, "th number:", smallest_index(arr, k))
