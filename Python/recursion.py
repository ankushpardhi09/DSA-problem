#when the many problems are divided into smaller subproblems, it is called recursion. 
#It is a powerful technique that allows us to solve complex problems by breaking them down into simpler ones.
#In Python, we can use recursion to solve a wide range of problems, from simple mathematical calculations to complex data structures.
#recurion is use stack memory to store the function calls, so it is important to be careful when using recursion to avoid hitting the 
#maximum recursion depth limit.

#what is difference between iteration and recursion?
#iteration is a process of repeating a block of code until a certain condition is met, while recursion is a process of calling a function 
#within itself to solve a problem.
#iteration uses loops to repeat a block of code, while recursion uses function calls to repeat a block of code.
#iteration is generally more efficient than recursion in terms of memory usage, as it does not require the overhead of function calls and 
#stack memory. However, recursion can be more elegant and easier to read in some cases, especially when dealing with problems that have a 
#natural recursive structure, such as tree traversal or factorial calculation.
#In summary, iteration and recursion are both powerful techniques for solving problems in Python, and the choice between them depends on the 
#specific problem being solved and the programmer's preference for code readability and efficiency.

# def factorial(num):
#     if num <= 1:#base case for the recursion, if the number is less than or equal to 1, return 1
#         return 1
#     return num * factorial(num - 1)
    
# print(factorial(5))

#5*factorial(4) = 5*4*factorial(3) = 5*4*3*factorial(2) = 5*4*3*2*factorial(1) = 5*4*3*2*1 = 120

#capitalizfirst solution using recursion
# def capitalizeFirst(arr):
#     result = []
#     if len(arr) == 0:  # base case: empty array
#         return result

#     first = arr[0]
#     if first:  # guard against empty strings
#         result.append(first[0].upper() + first[1:])
#     else:
#         result.append(first)

#     return result + capitalizeFirst(arr[1:])  # recursive call with the rest of the array
# print(capitalizeFirst(['car', 'taco', 'banana']))


# def power(base, exponent):
#     if exponent == 0:  # base case: any number to the power of 0 is 1
#         return 1
#     return base * power(base, exponent - 1)  # recursive call with the exponent decremented by 1

# print(power(2, 0))  # Output: 1
# print(power(2, 2))  # Output: 4
# print(power(2, 4))  # Output: 16
# #2*power(2, 0) = 2*1 = 1
# #2*power(2, 1) = 2*2*power(2, 0) = 2*2*1 = 4
# #2*power(2, 3) = 2*2*power(2, 2) = 2*2*4 = 16

# def productOfArray(arr):
#     if len(arr) == 0:  # base case: empty array
#         return 1
#     return arr[0] * productOfArray(arr[1:])  # recursive call with the rest of the array

# print(productOfArray([1, 2, 3]))  # Output: 6
# print(productOfArray([1, 2, 3, 10]))  # Output: 60
# #1*productOfArray([2, 3]) = 1*2*productOfArray([3]) = 1*2*3*productOfArray([]) = 1*2*3*1 = 6
# #1*productOfArray([2, 3, 10]) = 1*2*productOfArray([3, 10]) = 1*2*3*productOfArray([10]) = 1*2*3*10*productOfArray([]) = 1*2*3*10*1 = 60

# def reverse(string):
#     if len(string) == 1:  # base case: empty string
#         return string
#     return string[len(string)-1] + reverse(string[0:len(string)-1])  # recursive call with the string excluding the last character

# print(reverse('awesome'))  # Output: 'emosewa'
# print(reverse('python'))  # Output: 'nohtyp'
# #reverse('awesome') = 'e' + reverse('awesom') = 'e' + 'm' + reverse('aweso') = 'e' + 'm' + 'o' + reverse('awes') = 'e' + 'm' + 'o' + 's' + reverse('awe') = 'e' + 'm' + 'o' + 's' + 'e' + reverse('aw') = 'e' + 'm' + 'o' + 's' + 'e' + 'w' + reverse('a') = 'e' + 'm' + 'o' + 's' + 'e' + 'w' + 'a'
# #reverse('python') = 'n' + reverse('pytho') = 'n' + 'o' + reverse('pyth') = 'n' + 'o' + 'h' + reverse('pyt') = 'n' + 'o' + 'h' + 't' + reverse('py') = 'n' + 'o' + 'h' + 't' + 'y' + reverse('p') = 'n' + 'o' + 'h' + 't' + 'y' + 'p'


# def recursiveRange(num):
#     if num <= 0 :
#         return 0
#     return num + recursiveRange(num -1)

# print(recursiveRange(6))
# #recursiveRange(6) = 6 + recursiveRange(5) = 6 + 5 + recursiveRange(4) = 6 + 5 + 4 + recursiveRange(3) = 6 + 5 + 4 + 3 + recursiveRange(2) = 6 + 5 + 4 + 3 + 2 + recursiveRange(1) = 6 + 5 + 4 + 3 + 2 + 1 + recursiveRange(0) = 6 + 5 + 4 + 3 + 2 + 1 + 0 = 21


# def isPalindrome(string):
#     if len(string) == 0:  # base case: empty string or single character is a palindrome
#         return True
#     if string[0] != string[len(string)-1]:  # if the first and last characters are different, it's not a palindrome
#         return False
#     return isPalindrome(string[1:-1])  # recursive call with the string excluding the first and last characters

# print(isPalindrome('awesome'))  # Output: False
# print(isPalindrome('foobar'))  # Output: False
# #isPalindrome('awesome') = 'a' != 'e' => False
# #isPalindrome('foobar') = 'f' != 'r' => False

# someRecursive Solution using recursion

# def someRecursive(arr, callback):
#     if len(arr) == 0:  # base case: empty array
#         return False
#     if not(callback(arr[0])):  # if the callback returns False for the first element, check the rest of the array
#         return someRecursive(arr[1:], callback)  # recursive call with the rest of the array
#     return True  # if the callback returns True for the first element, return True

# def isOdd(num):
#     if num % 2 == 0:
#         return False
#     else:
#         return True
    
# print(someRecursive([1, 2, 3, 4], isOdd))  # Output: True
# print(someRecursive([4, 6, 8], isOdd))  # Output: False
#someRecursive([1, 2, 3, 4], isOdd) = isOdd(1) => True
       