#Selection sort
# time complexity: O(n^2)
# space complexity: O(1)

# input = [20, 12, 10, 15, 2]
# output = [2, 10, 12, 15, 20]

arr = [ 20, 12, 10, 15, 2]
for i in range(len(arr)):
    min = i
    j = i + 1
    while j < len(arr):
        if arr[j] < arr[min]:
            min = j
        j += 1
    arr[i],arr[min] = arr[min],arr[i]
print(arr)