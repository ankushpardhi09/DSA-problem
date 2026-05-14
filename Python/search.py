#Linear Search
# time complexity: O(n)
# space complexity: O(1)

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

array = [1, 2, 3, 4, 8, 7, 9]
target = 7 
result = linear_search(array,target)
if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found in the array.")
