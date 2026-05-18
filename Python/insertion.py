#Insertion sort
# time complexity: O(n^2)
# space complexity: O(1)

#input = [20, 12, 10, 15, 2]
#output = [2, 10, 12, 15, 20]

arr = [ 20, 12, 10, 15, 2]
for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1
    while j >= 0 and key < arr[j]:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key
print(arr)