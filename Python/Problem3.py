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

def smallest_missing_positive(nums):
    n = len(nums)
    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i]-1] != nums[i]:
            # Swap nums[i] with nums[nums[i]-1]
            nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1    
    return n + 1
# Example usage
nums = [7, 8, 9, 11, 12]    
result = smallest_missing_positive(nums)
print(result)  # Output: 1



