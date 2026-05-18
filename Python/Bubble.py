# Algorithm: Bubble Sort
# Time Complexity: O(n^2)
# Space Complexity: O(1)
#what is bubble sort? # Bubble Sort is a simple sorting algorithm that repeatedly steps through the list,start form the second element, 
# compares adjacent elements and swaps them if they are in the wrong order. The process is repeated until the list is sorted.

# Example:
# Input: [5,3,8,6,2]
# Output: [2,3,5,6,8]
# steps 1:
#Start always in the Second Element and compare it with the previous one, if the previous one is greater than the current one, swap them.
# i = 1, compare 3 with 5, since 5 is greater than 3, swap them. The list becomes [3,5,8,6,2]
# i = 2, compare 8 with 5, since 5 is not greater than 8, do nothing. The list remains [3,5,8,6,2]
# i = 3, compare 6 with 8, since 8 is greater than 6, swap them. The list becomes [3,5,6,8,2]
# i = 4, compare 2 with 8, since 8 is greater than  2, swap them. The list becomes [3,5,6,2,8]
# steps 2:
# i = 1, compare 5 with 3, since 3 is not greater than 5, do nothing. The list remains [3,5,6,2,8]
# i = 2, compare 6 with 5, since 5 is not greater than 6, do nothing. The list remains [3,5,6,2,8]
# i = 3, compare 2 with 6, since 6 is greater than 2, swap them. The list becomes [3,5,2,6,8]
# i = 4, compare 8 with 6, since 6 is not greater than 8, do nothing. The list remains [3,5,2,6,8]
# steps 3: 
# i = 1, compare 5 with 3, since 3 is not greater than 5, do nothing. The list remains [3,5,2,6,8]
# i = 2, compare 2 with 5, since 5 is greater than 2, swap them. The list becomes [3,2,5,6,8]
# i = 3, compare 6 with 5, since 5 is not greater than 6, do nothing. The list remains [3,2,5,6,8]
# i = 4, compare 8 with 6, since 6 is not greater than 8, do nothing. The list remains [3,2,5,6,8]
# steps 4:
# i = 1, compare 2 with 3, since 3 is greater than 2, swap them. The list becomes [2,3,5,6,8]
# i = 2, compare 5 with 3, since 3 is not greater than 5, do nothing. The list remains [2,3,5,6,8]
# i = 3, compare 6 with 5, since 5 is not greater than 6, do nothing. The list remains [2,3,5,6,8]
# i = 4, compare 8 with 6, since 6 is not greater than 8, do nothing. The list remains [2,3,5,6,8]


arr = [5,3,8,6,2]
for i in range(1, len(arr)):
    for j in range(0, len(arr)-i):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
print(arr)

# how to process this code 
# i = 1, key = 3, j = 0, compare 3 with 5, since 5 is greater than 3, move 5 to the right. The list becomes [5,5,8,6,2]
# j = -1, since j is less than 0, exit the while loop and insert 3 at the correct position. The list becomes [3,5,8,6,2]
# i = 2, key = 8, j = 1, compare 8  with 5, since 5 is not greater than 8, exit the while loop and insert 8 at the correct position. 
# The list remains [3,5,8,6,2]
# i = 3, key = 6, j = 2, compare 6 with 8, since 8 is greater than 6, move 8 to the right. The list becomes [3,5,8,8,2]
# j = 1, compare 6 with 5, since 5 is not greater than 6, exit the while loop and insert 6 at the correct position. The list becomes [3,5,6,8,2]
# i = 4, key = 2, j = 3, compare 2 with 8, since 8 is greater than 2, move 8 to the right. The list becomes [3,5,6,8,8]
# j = 2, compare 2 with 6, since 6 is greater than 2, move 6 to the right. The list becomes [3,5,6,6,8]
# j = 1, compare 2 with 5, since 5 is greater than 2, move 5 to the right. The list becomes [3,5,5,6,8]
# j = 0, compare 2 with 3, since 3 is greater than 2, move 3 to the right. The list becomes [3,3,5,6,8]
# j = -1, since j is less than 0, exit the while loop and insert 2 at the correct position. The list becomes [2,3,5,6,8]

