#remove Leading Zeros form a list of Integers
#input = [0,0,1,2,3,0,0,4]
#output = [1,2,3,0,0,4]

# def removeLeadingZeros(arr):
#     # Find the index of the first non-zero element
#     first_non_zero_index = 0
#     while first_non_zero_index < len(arr) and arr[first_non_zero_index] == 0:
#         first_non_zero_index += 1

#     # Return the sublist starting from the first non-zero element
#     return arr[first_non_zero_index:]
# # Example usage
# arr = [0, 0, 1, 2, 3, 0, 0, 4]
# result = removeLeadingZeros(arr)
# print(result)  # Output: [1, 2, 3, 0, 0, 4]


#first the First missing positive integer 

# input = [3, 4, -1, 1]
# output = 2

# def first_miss_positive(nums):
#     n = len(nums)
#     for i in range(n):
#         while 1 <= nums[i] <= n and nums[nums[i]-1] != nums[i]:
#             # Swap nums[i] with nums[nums[i]-1]
#             nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
#     for i in range(n):
#         if nums[i] != i + 1:
#             return i + 1    
#     return n + 1
# # Example usage
# nums = [3, 4, -1, 1]
# result = first_miss_positive(nums)
# print(result)  # Output: 2

#Find the smallest missing positive integer.

#input = [7,8,9,11,12]
#output = 1

# def smallest_missing_positive(nums):
#     n = len(nums)
#     for i in range(n):
#         while 1 <= nums[i] <= n and nums[nums[i]-1] != nums[i]:
#             # Swap nums[i] with nums[nums[i]-1]
#             nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
#     for i in range(n):
#         if nums[i] != i + 1:
#             return i + 1    
#     return n + 1
# # Example usage
# nums = [7, 8, 9, 11, 12]    
# result = smallest_missing_positive(nums)
# print(result)  # Output: 1


#permutation in input = [1,2,3]
#output = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#With simple logic
#Algorithm:
#1. We define a helper function backtrack that takes the current index (start) as an argument.
#2. If the current index is equal to the length of the input list, it means we have generated a complete permutation, so we add a copy of the current list to the result.
#3. We iterate through the list starting from the current index (start) to the end of the list.
#4. For each iteration, we swap the current index with the index of the iteration (i) to generate a new permutation.
#5. We then recursively call the backtrack function with the next index (start + 1) to continue generating permutations.
#6. After the recursive call, we swap back the elements to restore the original list for the next iteration (backtracking).


def permute(nums):
    result = []
    def backtrack(start):
        if start == len(nums):
            result.append(nums[:])
            return
        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]  # Swap
            backtrack(start + 1)  # Recurse
            nums[start], nums[i] = nums[i], nums[start]  # Backtrack
    backtrack(0)
    return result
# Example usage
nums = [1, 2, 3]
result = permute(nums)
print(result)  # Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]


#combinations of a list of integers
#input = [1,2,3]
#output = [[],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]]
#Algorithm:
#1. We define a helper function backtrack that takes the current index (start) and the current combination (path) as arguments.
#2. We add the current combination (path) to the result list.
#3. We iterate through the list starting from the current index (start) to the end of the list.
#4. For each iteration, we add the current element (nums[i]) to the current combination (path) and recursively call the backtrack function with the next index (i + 1) to continue generating combinations.
#5. After the recursive call, we remove the last element from the current combination (path .pop()) to backtrack and explore other combinations.

def combinations(nums):
    result = []
    def backtrack(start, path):
        result.append(path[:])  # Add the current combination to the result
        for i in range(start, len(nums)):
            path.append(nums[i])  # Include nums[i] in the current combination
            backtrack(i + 1, path)  # Recurse with the next index
            path.pop()  # Backtrack by removing the last element
    backtrack(0, [])
    return result   
# Example usage
nums = [1, 2, 3]
result = combinations(nums)
print(result)  # Output: [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
    
