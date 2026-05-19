#find the First Non-Repeating Character in a String

# s = "leetcode"
# output: l

# def firstUniqChar(s):
#     char_count = {}
    
#     # Count the occurrences of each character
#     for char in s:
#         if char in char_count:
#             char_count[char] += 1
#         else:
#             char_count[char] = 1
            
#     # Find the first non-repeating character
#     for char in s:
#         if char_count[char] == 1:
#             return char
            
#     return None  # Return None if there is no non-repeating character   

# s = "leetcode"
# result = firstUniqChar(s)
# print(result)


# choose two cards. To win the game, the product of the values of the two cards must be the
# maximum value possible for any pair of cards in the display, The winning amount willbe the sum
# of the two cards chosen by the player, 
# Wite an algorithm to find the winning amount as the sum of the values of the two cards whose product value is maximum.
# Input
# The first line of the input consists of an integer numCards, representing the number of cards (N).The second line consists of N space-separated integers ….., val1, val2.., alN representing the values on the cards.
# Output
# Print an integer representing the sum of the values of the two cards whose product value İs maximum.

#input = 7,9,-3,8,-6,-7,8,10
#output = 19

# def maxProductSum(numCards, cardValues):
#     if numCards < 2:
#         return None  # Not enough cards to choose from

#     max_product = float('-inf')# Initialize max_product to negative infinity to handle cases where all products are negative.
#     #-inf is a special value in Python that represents negative infinity. 
#     winning_sum = 0

#     for i in range(numCards):
#         for j in range(i + 1, numCards):
#             product = cardValues[i] * cardValues[j]
#             if product > max_product:
#                 max_product = product
#                 winning_sum = cardValues[i] + cardValues[j]

#     return winning_sum

# # Example usage
# numCards = 8
# cardValues = [7, 9, -3, 8, -6, -7, 8, 10]
# result = maxProductSum(numCards, cardValues)
# print(result)  # Output: 19
# # cardValues[1] * cardValues[7] = 9 * 10 = 90, which is the maximum product, and their sum is 9 + 10 = 19


#Array Rotation

# input = [1, 2, 3, 4, 5] roteted by 2 steps
# output = [4, 5, 1, 2, 3]

def rotateArray(arr, steps):
    steps = steps % len(arr)  # Handle cases where steps is greater than array length
    return arr[-steps:] + arr[:-steps]

print(rotateArray([1, 2, 3, 4, 5], 2))  # Output: [4, 5, 1, 2, 3]

